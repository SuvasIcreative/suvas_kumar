# -*- coding: utf-8 -*-

from odoo import fields, models, api




class SaleOderInherit(models.Model):
    _inherit = 'sale.order'

    expect_time_slot = fields.Char(string='Expected Time Slot')
    customer_comment = fields.Html(string='Customer Comment For Delivery')
