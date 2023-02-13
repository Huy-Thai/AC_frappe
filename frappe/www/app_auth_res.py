import frappe
from frappe import _

no_cache = True

def get_context(context):
	context.no_header = True
	context["title"] = "App Auth Response"
	context["hide_login"] = True
	context["user_context"] = frappe.session
	context["logo"] = frappe.get_website_settings("app_logo") or frappe.get_hooks("app_logo_url")[-1]
	context["app_name"] = (
		frappe.get_website_settings("app_name") or frappe.get_system_settings("app_name") or _("Frappe")
	)

	return context
