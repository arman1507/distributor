// Copyright (c) 2020, arman and contributors
// For license information, please see license.txt

frappe.ui.form.on('Purchase Order DIstributor', {
	refresh: function(frm) {
		cur_frm.get_field("items").grid.toggle_reqd("delivery_date", true);
	}
});
frappe.ui.form.on('Sales Order Item', {
	// refresh: function(frm,cdt,cdn){
	
	// },
	item_code:function(frm,cdt,cdn){
		var child = locals[cdt][cdn];
		child.qty = 1;
		child.rate = 2000;
		let amount = child.qty * child.rate;
		child.conversion_factor = child.qty;
		child.amount = amount;
		cur_frm.refresh_field("items");
	},
	qty:function(frm,cdt,cdn){
		var child = locals[cdt][cdn];
		let amount = child.qty * child.rate;
		child.conversion_factor = child.qty;
		child.amount = amount;
		cur_frm.refresh_field("items");
	},
	rate:function(frm,cdt,cdn){
		var child = locals[cdt][cdn];
		let amount = child.qty * child.rate;
		child.amount = amount;
		cur_frm.refresh_field("items");
	}
});
