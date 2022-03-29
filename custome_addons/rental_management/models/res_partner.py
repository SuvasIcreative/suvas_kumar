# -*- coding: utf-8 -*-

from odoo import fields, models, api,_
from odoo.exceptions import UserError, ValidationError



class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_rank = fields.Integer(string="Customer Rank", required=False)

    @api.constrains('customer_rank')
    def _constrains_set_limit_rank(self):
        if self.customer_rank not in range(1,11):
            raise UserError('Give Rank out of 10')

