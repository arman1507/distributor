frappe.listview_settings['Purchase Order DIstributor'] = {
	onload: function(listview) {
		// if (!frappe.route_options){ //remove this condition if not required
			frappe.route_options = {
				"nama": ["=", frappe.session.user_fullname]
			};
		// }
	}
};