# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_taxcloud"
app_title = "ERPNext TaxCloud"
app_publisher = "Neil Lasrado"
app_description = "Fetches United State sales tax from TaxCloud.com and updates Quotations, Sales Order & Sales Invoice"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "neil@digithinkit.com"
app_license = "MIT"

doc_events = {
	"Quotation" : {
		"validate": "erpnext_taxcloud.api.set_sales_tax"
	}
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_taxcloud/css/erpnext_taxcloud.css"
# app_include_js = "/assets/erpnext_taxcloud/js/erpnext_taxcloud.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_taxcloud/css/erpnext_taxcloud.css"
# web_include_js = "/assets/erpnext_taxcloud/js/erpnext_taxcloud.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_taxcloud.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_taxcloud.install.before_install"
# after_install = "erpnext_taxcloud.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_taxcloud.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_taxcloud.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_taxcloud.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_taxcloud.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_taxcloud.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_taxcloud.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_taxcloud.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_taxcloud.event.get_events"
# }

