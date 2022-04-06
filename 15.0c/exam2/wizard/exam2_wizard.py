# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime




class SaleOrder1Wizard(models.TransientModel):
    _name = 'sale_order_wizard'
    _description = 'sale.order.wizard'

    product_order_line_ids = fields.One2many(comodel_name='sale1_order_wizard',
                                             inverse_name="product_order_line_id",
                                             string='Product')


    #
    def create_order_line(self):
        print("hello")
        for rec in self:
            for res_id in [(self._context['current_id'])]:
                for ids in res_id:

                    vals = {'partner_id': ids
                            }
                    order = self.env['sale.order'].create(vals)
    #
                    for product in rec.product_order_line_ids:
                        order.write({'order_line': [(0, 0, product)]})

