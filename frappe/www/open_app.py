import frappe
from frappe import _

no_cache = True

def get_context(context):
	context.no_header = True
	context["title"] = "Open ERP Desktop App"
	context["hide_login"] = True
	context["user_context"] = frappe.session

	return context
