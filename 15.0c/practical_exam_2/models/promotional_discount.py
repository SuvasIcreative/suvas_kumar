# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from datetime import datetime
from odoo.exceptions import UserError, ValidationError



class PromotionalDiscount(models.Model):
    _name = 'promotional.discount'
    _description = 'promotional discount details'

    name = fields.Char(string="Name", required=True)
    discount_type = fields.Selection([('percentage', 'Percentage'), ('fixed_amount', 'Fixed Amount')], default="fixed_amount")
    currency_id = fields.Many2one('res.currency')
    discount = fields.Float()
    minimum_order_amount = fields.Float(string='Minimum Order Amount', default=100)
    start_date = fields.Datetime(string='Start Date', default=datetime.now(), readonly=False)
    end_date = fields.Datetime(string="End Date", required=True)

    @api.constrains('end_date', 'start_date')
    def date_constrains(self):
        for rec in self:
            if rec.end_date < rec.start_date:
                raise ValidationError(_('Sorry, End Date Must be greater Than Start Date...'))

    @api.onchange('discount_type')
    def check_discount_type(self):
        currency = self.env['res.currency']
        for rec in self:
            if rec.discount_type == 'fixed_amount':
                rec.currency_id = currency.search([('name', '=', 'USD')])
            elif rec.discount_type == 'percentage':
                rec.currency_id = currency.search([('name', '=', 'PER')])
            else:
                rec.currency_id = False
