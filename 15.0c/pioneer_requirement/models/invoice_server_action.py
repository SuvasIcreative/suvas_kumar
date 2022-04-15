# -*- coding: utf-8 -*-

from odoo import fields, models, api


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'


    def generate_subscription_bill(self):
        res = []
        for record in self.invoice_line_ids:
            if record.vendor_id not in res:
                res.append(record.vendor_id)
                a = self.create({'move_type': 'in_invoice',
                                'partner_id': record.vendor_id})
                line_ids = self.invoice_line_ids.search([('vendor_id', '=', record.vendor_id.id),
                                                         ('id', 'in', [line.id for line in self.invoice_line_ids])])
                print(line_ids)
                for line_id in line_ids:
                    a.write({'invoice_line_ids': [(0, 0, {'product_id': line_id.product_id,
                                                          'price_unit': line_id.vendor_price,
                                                          'quantity': line_id.quantity,
                                                          'delivery_address_id': line_id.delivery_address_id,
                                                          'planned_gp': line_id.planned_gp})]})
