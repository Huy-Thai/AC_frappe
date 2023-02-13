window.login = {};

login.bind_events = function () {
	$(window).on("hashchange", function () {
		login.route();
	});

	$(".form-login").on("submit", function (event) {
		event.preventDefault();
        let headers = frappe.request.headers;
		console.log(headers);
    	window.document = `unilinks://erpnext-dev.pandion.vn/?headers=${headers}`;
		
		return false;
	});
}

frappe.ready(function () {
	login.bind_events();
});
