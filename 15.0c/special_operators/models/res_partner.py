# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import UserError



class ResPartner(models.Model):
    _inherit = 'res.partner'


    @api.constrains('customer_rank')
    def _constrains_set_limit_rank(self):
        if self.customer_rank not in range(1,11):
            raise UserError('Give Rank out of 10')

