# -*- coding: utf-8 -*-

from odoo import fields, models, api,_
from odoo.exceptions import UserError, ValidationError



class ResPartner(models.Model):
    _inherit = 'res.partner'

    # customer_rank = fields.Integer(string="Customer Rank", required=False)
    #
    # @api.constrains('customer_rank')
    # def _constrains_set_limit_rank(self):
    #     if self.customer_rank not in range(1,11):
    #         raise UserError('Give Rank out of 10')

    # @api.onchange('partner_id')
    # def _onchange_customer_rank(self):
    #     if self.customer_rank >= 5:
    #         self.write({'category_id': [(4, 9)]})
    #     else:
    #         self.write({'category_id': [(2, 9)]})



    # def action_update_some_field(self):
    #     self.write({'name':'selmon boi','phone':'910639255','email':'semon@1235','model':'54679777734'})
