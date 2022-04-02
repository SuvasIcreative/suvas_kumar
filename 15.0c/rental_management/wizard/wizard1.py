# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder1Wizard(models.TransientModel):
    _name = 'sale.order1.wizard'
    _description = 'sale.order1.wizard'

    product_ids = fields.Many2many('product.product',string="Product ids")




    def create_order_line(self):
        context = self.env.context
        active_ids = context.get('active_ids')
        # print(active_ids)
        rec = self.env['sale.order'].browse(active_ids)
        # print(id)
        # for sale_rec in self.product_ids:
        #     # ids.write({'order_line':[(4,sale_rec.id)]})
        #     ids.write({'order_line':[(0,0,{'product_id':sale_rec.id,'product_uom_qty':10})]})

        order_lines = []
        for product in self.product_ids:
            order_lines.append((0, 0, {
                'product_id': product.id
            }))
        rec.write({'order_line': order_lines})