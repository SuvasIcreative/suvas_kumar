# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ContactSaleHistory(models.Model):
    _name = 'contact.sale.history'
    _description = 'create for contact sale one2many field'


    partner_sale_id = fields.Many2one('contact.sale')
    old_state = fields.Char()
    new_state = fields.Char()
    old_n_of_follow_ups = fields.Integer(string="Old Follow UPS")
    new_n_of_follow_ups = fields.Integer(string="New Follow UPS")
