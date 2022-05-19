# -*- coding: utf-8 -*-
"""This model for Inheriting sale order and stock picking """
from odoo import fields, models


class SaleOderInherit(models.Model):
    """ Inherit sale order Model """
    _inherit = 'sale.order'

    expect_time_slot = fields.Char(string='Expected Time Slot')
    customer_comment = fields.Html(string='Customer Comment For Delivery')

    def action_confirm(self):
        """ This Funtion for write Delivery Comment and Delivery
        Time Slot on stock picking modele"""
        super(SaleOderInherit, self).action_confirm()
        stock_picking_id = self.env['stock.picking'].search([('origin', '=', self.name)])
        stock_picking_id.write({'note': self.customer_comment,
                                'expect_time_slot': self.expect_time_slot})

class StockPickingInherit(models.Model):
    """ Inherit Stock picking Model"""
    _inherit = 'stock.picking'


    expect_time_slot = fields.Char(string='Expected Time Slot')
