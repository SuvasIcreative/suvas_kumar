# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import UserError


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'


    def generate_subscription_bill(self):
        record_state = self.search([('state', '=', 'posted'), ('id', 'in', [record.id for record in self])])
        for rec in self:
            if rec.move_type == 'out_invoice':
                if len(record_state) > 0:
                    if rec.state == 'posted':
                        res = []
                        for record in rec.invoice_line_ids:
                            if record.vendor_id not in res:
                                res.append(record.vendor_id)
                                line_ids = rec.invoice_line_ids.search([('vendor_id', '=',record.vendor_id.id),
                                                                        ('id', 'in', [line.id for line in
                                                                                      rec.invoice_line_ids])])
                                product = []
                                for line_id in line_ids:
                                    product.append((0, 0, {'product_id': line_id.product_id,
                                                           'price_unit': line_id.vendor_price,
                                                           'quantity': line_id.quantity,
                                                           'delivery_address_id': line_id.delivery_address_id,
                                                           'planned_gp': line_id.planned_gp}))
                                self.create({'move_type': 'in_invoice',
                                             'partner_id': record.vendor_id,
                                             'invoice_line_ids': product})
                else:
                    raise UserError('Invoice are not in posted state!')
            else:
                raise UserError('This Button work only for Invoice!')
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': 'account.action_move_in_invoice_type',
            'view_mode': 'tree,form'
        }











#
#
# res = []
#                         for record in self.invoice_line_ids:
#                             if record.vendor_id not in res:
#                                 # print("++++++++\n\n\n\n", record, '\n\n', record.vendor_id, '\n\n\n', record.vendor_id.id)
#                                 res.append(record.vendor_id)
#                                 bill_record_set = self.create({'move_type': 'in_invoice',
#                                                               'partner_id': record.vendor_id})
#                                 # print("bill_record_set__________\n\n\n",a,'\n\n\n',bill_record.id)
#                                 line_ids = self.invoice_line_ids.search([('vendor_id', '=', record.vendor_id.id),
#                                                                          ('id', 'in', [line.id for line in self.invoice_line_ids])])
#                                 # print("\n\n\nType", type(line_ids), "\n\n\n", line_ids)
#                                 print(line_ids)
#                                 for line_id in line_ids:
#                                     print("line_id\n\n\n",line_id)
#                                     bill_record_set.write({'invoice_line_ids':
#                                                           [(0, 0, {'product_id': line_id.product_id,
#                                                                    'price_unit': line_id.vendor_price,
#                                                                    'quantity': line_id.quantity,
#                                                                    'delivery_address_id': line_id.delivery_address_id,
#                                                                    'planned_gp': line_id.planned_gp})]})

