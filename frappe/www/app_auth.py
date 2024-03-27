import frappe
from frappe import _
from frappe.utils.html_utils import get_icon_html
from frappe.utils.password import get_decrypted_password
from frappe.utils.oauth import get_oauth2_authorize_url, get_oauth_keys
from frappe.website.utils import get_home_page

no_cache = True

def get_context(context):
	redirect_to = "/app_auth_res"
	context.no_header = True
	context["title"] = "App Auth"
	context["hide_login"] = True
	context["provider_logins"] = []
	context["logo"] = frappe.get_website_settings("app_logo") or frappe.get_hooks("app_logo_url")[-1]
	context["app_name"] = (
		frappe.get_website_settings("app_name") or frappe.get_system_settings("app_name") or _("Frappe")
	)

	if cint(frappe.db.get_value("LDAP Settings", "LDAP Settings", "enabled")):
		from frappe.integrations.doctype.ldap_settings.ldap_settings import LDAPSettings

		context["ldap_settings"] = LDAPSettings.get_ldap_client_settings()

	# providers = frappe.get_all(
	# 	"Social Login Key",
	# 	filters={"enable_social_login": 1},
	# 	fields=["name", "client_id", "base_url", "provider_name", "icon"],
	# 	order_by="name",
	# )

	# for provider in providers:
	# 	client_secret = get_decrypted_password("Social Login Key", provider.name, "client_secret")
	# 	if not client_secret:
	# 		continue

	# 	icon = None
	# 	if provider.icon:
	# 		if provider.provider_name == "Custom":
	# 			icon = get_icon_html(provider.icon, small=True)
	# 		else:
	# 			icon = f"<img src='{provider.icon}' alt={provider.provider_name}>"

	# 	if provider.client_id and provider.base_url and get_oauth_keys(provider.name):
	# 		context.provider_logins.append(
	# 			{
	# 				"name": provider.name,
	# 				"provider_name": provider.provider_name,
	# 				"auth_url": get_oauth2_authorize_url(provider.name, redirect_to),
	# 				"icon": icon,
	# 			}
	# 		)
	# 		context["social_login"] = True

	return context
