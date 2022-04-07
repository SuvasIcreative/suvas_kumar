# -*- coding: utf-8 -*-

from odoo import models, fields, api




class SaleOrderLineWizard(models.TransientModel):
    _name = 'sale.order.line.wizard'
    _description = 'Create Oder Line'

    product_order_line_id = fields.Many2one(comodel_name='sale.order.product.wizard')
    product_id = fields.Many2one(comodel_name='product.product', string="Product")
    product_quantity = fields.Float(string='Quantity')
    price = fields.Float(related="product_id.list_price", string='Price')


