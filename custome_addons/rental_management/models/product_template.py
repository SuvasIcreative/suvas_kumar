# -*- coding: utf-8 -*-

from odoo import fields, models,api


# Sales module extensions
class ProductTemplate(models.Model):
    # """ Sales Module Extension """
    _inherit = 'product.template'

    is_rental = fields.Boolean(string="Is Rental")
    rental_type = fields.Many2one('rental.type', string='Rental Type')



