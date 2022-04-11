# -*- coding: utf-8 -*-

from odoo import fields, models, api,_


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def send_mail(self):
        print("Hey", '\n\n\n')
