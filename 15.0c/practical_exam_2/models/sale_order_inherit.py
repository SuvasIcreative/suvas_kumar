# -*- coding: utf-8 -*-

from odoo import fields, models, api,_


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    promotional_discount_check = fields.Boolean(compute="promo_discount_check")


    def promo_discount_check(self):
        rec = self.env['ir.config_parameter'].sudo()
        self.promotional_discount_check = rec.get_param('practical_exam_2.promotional_discount')

    def action_apply_promotional_discount(self):
        print("HEllo")
