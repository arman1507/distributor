# -*- coding: utf-8 -*-
# Copyright (c) 2020, arman and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import utils

class PurchaseOrderDIstributor(Document):
	def on_submit(self):
		so = frappe.new_doc('Sales Order')
		so.customer = self.customer
		so.order_type = self.order_type
		so.company = self.company
		so.transaction_date = utils.today()
		so.currency = 'IDR'
		so.conversion_date = 1
		so.plc_conversion_date = 1
		so.status = 'Draft'
		so.selling_price_list = 'Standard Selling'
		so.price_list_currency = 'IDR'
		for i in self.items:
			so.append('items',{
				'item_code': i.item_code,
				'item_name': i.item_name,
				'description' : i.description,
				'delivery_date': i.delivery_date,
				'qty':i.qty,
				'uom':i.uom,
				'conversion_factor': i.conversion_factor
			})
		so.save()
		so.submit()