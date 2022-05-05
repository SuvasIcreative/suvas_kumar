# -*- coding: utf-8 -*-

from odoo import fields, models, api,_


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def action_apply_promotional_discount(self):
        print("HEllo")