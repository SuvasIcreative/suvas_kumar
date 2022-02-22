# -*- coding: utf-8 -*-

from odoo import fields, models


# Sales module extensions
class ResPartner(models.Model):
    # """ Sales Module Extension """
    _inherit = 'res.partner'

    dob = fields.Date(string="DOB", required=False)
    customer_r = fields.Char(string='Custer_Reference')
