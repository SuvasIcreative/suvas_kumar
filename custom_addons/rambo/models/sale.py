# -*- coding: utf-8 -*-

from odoo import fields, models, api


# Sales module extension
class sale(models.Model):
    # """ Sales Module Extension """
    _inherit = 'sale.order'  # Seller
    # x_salesm = fields.Many2one('res.users', string='Salesman', related='partner_id.user_id')
    customer_reference = fields.Char(string='Custer_Reference', related='partner_id.customer_r',)
    date_of_birth = fields.Date(string="Date Of Birth", required=False,related='partner_id.dob',)

