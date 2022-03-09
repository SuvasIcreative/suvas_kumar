# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RentalType(models.Model):
    _name = 'rental.type'
    _description = 'rental.type'

    name = fields.Char(string="Name")
    code=fields.Char(string='Code')
    description=fields.Text(string='Description')

