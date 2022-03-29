# -*- coding: utf-8 -*-

from odoo import fields, models, api,_
from odoo.exceptions import UserError, ValidationError




class ResPartner(models.Model):
    _inherit = 'sale.order'

    customer_rank = fields.Integer(related='partner_id.customer_rank', string="Customer Rank", required=False)
    stare = fields.Selection([('a', '1'), ('b', '2'), ('c', '3'),
                              ('d', '4'), ('e', '5'), ('f', '6'),
                              ('g', '7'), ('h', '8'), ('i', '9'),
                              ('j', '10'), ('k', '11')], string=" ")

    @api.onchange('partner_id')
    def _onchange_customer_rank(self):
        if self.customer_rank >= 5:
            self.write({'tag_ids': [(4, 9, 0)]})
        # else:
        #     self.write({'tag_ids':[(2,9,0)]})
    # @api.depends("customer_rank")
    # def _calculate_rank(self):
    #     if self.customer_rank:
    #         for recode
    #             , compute = "_calculate_rank"

    # @api.model
    # def default_get(self,field_list=[]):
    #     res=super(rental_management, self).default_get(field_list)
    #     res['name']='Adrash'
    #     return res
    # @api.onchange('customer_id')
    # def _onchange_phone_number(self):