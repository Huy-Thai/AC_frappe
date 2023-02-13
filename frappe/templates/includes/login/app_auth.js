window.login = {};

login.bind_events = function () {
	$(window).on("hashchange", function () {
		login.route();
	});

	$(".form-login").on("submit", function (event) {
		event.preventDefault();
        let cookies = frappe.get_cookies();
		console.log(cookies);
        window.location = `start "unilinks://erpnext-dev.pandion.vn/?userId=${cookies.user_id}"`
		
		return false;
	});
}

frappe.ready(function () {
	login.bind_events();
});
