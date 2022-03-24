# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RentalType(models.Model):
    _name = 'rental.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'rental.type'

    name = fields.Char(string="Name", required=True, tracking=True)
    code = fields.Char(string='Code', required=True, tracking=True)
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('code_uniq', 'unique (code)', 'The code  must be unique per person !')
    ]
