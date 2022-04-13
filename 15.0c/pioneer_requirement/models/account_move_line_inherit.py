# -*- coding: utf-8 -*-

from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    delivery_address_id = fields.Many2one(comodel_name='res.partner', string="Delivery Address",
                                          domain=[('type', '=', 'delivery')])
    vendor = fields.Many2one(comodel_name='res.partner', string='Vendor',
                             domain=[('supplier_rank', '>', '0')])
    vendor_price = fields.Float(string='Vendor Price')
    planned_gp = fields.Float(string='Planned GP%')
    description = fields.Char(string='Description',
                              compute='_compute_description')

    @api.onchange('vendor_price', 'price_unit')
    def calculated_planned_gp(self):
        for rec in self:
            if self.vendor_price and self.price_unit:
                rec.planned_gp = ((rec.price_unit-rec.vendor_price)/rec.price_unit)*100

    @api.depends('delivery_address_id', 'name')
    def _compute_description(self):
        for record in self:
            if record.name and record.delivery_address_id:
                record.description = "%s %s" % (record.delivery_address_id.name or ' ,', record.name)
                # print("\n\n\n", record.description)
            else:
                record.description = ''
