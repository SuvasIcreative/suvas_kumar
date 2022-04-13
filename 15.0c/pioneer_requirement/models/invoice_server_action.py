# -*- coding: utf-8 -*-

from odoo import fields, models, api


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'


    def generate_subscription_bill(self):
        print("\n\n\n", "hello")

