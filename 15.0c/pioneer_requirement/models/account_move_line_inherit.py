# -*- coding: utf-8 -*-

from odoo import fields, models, api,_


class ResPartner(models.Model):
    _inherit = 'account.move.line'

    delivery_address_id = fields.Many2one('res.partner', string="Delivery Address",
                                          domain=[('type', '=', 'delivery')])
    vendor = fields.Many2one('res.partner', string='Vendor',
                             domain=[('supplier_rank', '>', '0')])
    vendor_price = fields.Float(string='Vendor Price')
    planned_gp = fields.Float(string='Planned GP%')
    description = fields.Char(string='Description')

    @api.onchange('vendor_price','price_unit')
    def calculated_planned_gp(self):
        for rec in self:
            if self.vendor_price and self.price_unit:
                self.vendor_price = ((rec.price_unit-rec.vendor_price)/rec.price_unit)*100

        # ((Unit Price – vendor price) / Unit Price) * 100