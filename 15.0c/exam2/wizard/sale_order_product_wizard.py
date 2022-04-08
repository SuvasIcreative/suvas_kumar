# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime




class SaleOrderProductWizard(models.TransientModel):
    _name = 'sale.order.product.wizard'
    _description = 'Create Sale Oder Product'

    product_order_ids = fields.One2many(comodel_name='sale.order.line.wizard',
                                        inverse_name="product_order_line_id",
                                        string='Product')


    def create_sale_order(self):
        order_line = []
        sale_order = []

        for line in self.product_order_ids:
            order_line.append((0, 0, {'product_id': line.product_id.id,
                                      'product_uom_qty': line.product_quantity}))

        for res_id in [(self._context['current_id'])]:
            for ids in res_id:
                vals = {'partner_id': ids, 'order_line': order_line}
                sale_order.append(self.env['sale.order'].create(vals).id)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain':  [('id', 'in', sale_order)],
        }