window.login = {};

login.bind_events = function () {
	$(window).on("hashchange", function () {
		login.route();
	});

	$(".form-login").on("submit", function (event) {
		event.preventDefault();
        let cookies = "{{ user_context }}";
		console.log(cookies);
    	window.open(
			`unilinks://erpnext-dev.pandion.vn/?cookies=${cookies}`,
			'_blank',
		)
		
		return false;
	});
}

frappe.ready(function () {
	login.bind_events();
});
