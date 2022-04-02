# -*- coding: utf-8 -*-

from odoo import fields, models, api,_
from odoo.exceptions import UserError, ValidationError




class ResPartner(models.Model):
    _inherit = 'sale.order'

    # customer_rank = fields.Integer(related='partner_id.customer_rank', string="Customer Rank", required=False)

    # @api.onchange('partner_id')
    # def _onchange_customer_rank(self):
    #     print("+++++++++++++++++++++++++++++++++++++++++++++++=",self)
    #
    #     if self.env['res.partner'].customer_rank >= 5:
    #         print("__________________________________________")
    #         self.env['res.partner'].write({'category_id': [(4, 9)]})
    #     else:
    #         self.env['res.partner'].write({'category_id': [(2, 9)]})

    # @api.onchange('partner_id')
    @api.model
    def create(self, vals):
        res = super(ResPartner, self).create(vals)
        best_categ_id = self.env.ref("rental_management.res_partner_category_best_customer").id
        if res.partner_id.customer_rank > 5:
            print ("????????????", best_categ_id)
            res.partner_id.write(
                {'category_id': [(4, best_categ_id)]})
            # 4 - Link, best_categ_id - id of Best Customer tag
        else:
            res.partner_id.write(
                {'category_id': [(3, best_categ_id)]})
        return res




