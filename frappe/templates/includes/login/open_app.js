frappe.ready(() => {
	$(window).on("load", (_) => {
		window.open(
            'acerp-desk-app://res=openapp',
            '_blank',
        ).focus();
	});
});
