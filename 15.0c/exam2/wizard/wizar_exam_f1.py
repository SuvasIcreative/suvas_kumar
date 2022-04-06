# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime




class SaleOrder1Wizard(models.TransientModel):
    _name = 'sale1_order_wizard'
    _description = 'sale.order.wizard'

    product_order_line_id = fields.Many2one(comodel_name='sale_order_wizard')
    product_id = fields.Many2one(comodel_name='product.product', string="Product")
    product_quantity = fields.Float(string='Quantity', default=1)
    price = fields.Float(related="product_id.list_price", string='Price')


