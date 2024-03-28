const CryptoJS = require('crypto-js');

window.login = {};

login.bind_events = function () {
	$(window).on("hashchange", function () {
		login.route();
	});

	$(".form-login").on("submit", function (event) {
		event.preventDefault();
		const passphrase = 'ehb88S23us3XiaJWleYvPH2Bv8NgSIgp';
		let cookies = "{{ user_context }}";
		let encryptCookies = CryptoJS.AES.encrypt(cookies, passphrase).toString()

		window.open(
			`acerp-desk-app://res=${encryptCookies}`,
			'_blank',
		)

		return false;
	});
}

frappe.ready(function () {
	login.bind_events();
});
