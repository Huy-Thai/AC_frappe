frappe.ready(() => {
	$(window).on("load", (_) => {
		window.open(
            'acerp-desk-app-dev://res=openapp',
            '_blank',
        ).focus();
	});
});
