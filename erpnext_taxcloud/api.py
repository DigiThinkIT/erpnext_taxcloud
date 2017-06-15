import requests
import frappe
import hashlib
import json


def set_sales_tax(doc, method):
	taxcloud_settings = frappe.get_single("TaxCloud Settings")
	if not (taxcloud_settings.api_login_id or taxcloud_settings.api_key or taxcloud_settings.tax_account_head):
		return

	company_address = frappe.get_doc("Address", {"is_your_company_address": 1})
	if company_address and doc.shipping_address_name:
		shipping_address = frappe.get_doc("Address", doc.shipping_address_name)
	else:
		return

	if not shipping_address.country == "United States":
		return

	if (frappe.db.get_value("Quotation", doc.name, "address_display") == doc.address_display) \
		and (frappe.db.get_value("Quotation", doc.name, "total") == doc.total):
			return

	data = {
		"apiLoginId": taxcloud_settings.api_login_id,
		"customerID": hashlib.sha224(doc.customer).hexdigest()[:12],
		"origin": {
			"Address1": company_address.address_line1,
			"Address2": company_address.address_line2,
			"City": company_address.city,
			"State": company_address.state,
			"Zip5": company_address.pincode
		},
		"cartItems": [],
		"destination": {
			"City": shipping_address.city,
			"State": shipping_address.state,
			"Zip5": shipping_address.pincode
		},
		"cartID": doc.name,
		"deliveredBySeller": "true" if taxcloud_settings.delivered_by_seller else "false",
		"apiKey": taxcloud_settings.get_password("api_key")
	}

	index = 0
	for item in doc.items:
		data["cartItems"].append({
			"Index": index,
			"ItemID": item.item_code,
			"TIC": 00000,
			"Price": item.rate,
			"Qty": item.qty,
		})
		index += 1

	r = requests.post(
		"https://api.taxcloud.net/1.0/TaxCloud/Lookup", json=data)
	if r.text:
		tax_amount = 0
		for item in json.loads(r.text).get("CartItemsResponse"):
			tax_amount += item.get("TaxAmount")
		if "Sales Tax" in [tax.description for tax in doc.taxes]:
			for tax in doc.taxes:
				if tax.description == "Sales Tax":
					tax.tax_amount = tax_amount
					break

		elif tax_amount > 0:
			doc.append("taxes", {
				"charge_type": "Actual",
				"description": "Sales Tax",
				"account_head": taxcloud_settings.tax_account_head,
				"tax_amount": tax_amount
			})
		doc.run_method("calculate_taxes_and_totals")
