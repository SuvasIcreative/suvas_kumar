# -*- coding: utf-8 -*-

from odoo import fields, models, api,_




class ResPartner(models.Model):
    _inherit = 'sale.order'


    @api.model
    def create(self, vals):
        res = super(ResPartner, self).create(vals)
        b_customer_id = self.env.ref("rental_management.res_partner_category_best_customer").id
        if res.partner_id.customer_rank > 5:
            res.partner_id.write(
                {'category_id': [(4,b_customer_id)]})
        else:
            res.partner_id.write(
                {'category_id': [(3, b_customer_id)]})
        return res




