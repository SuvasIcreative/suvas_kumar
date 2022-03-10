# -*- coding: utf-8 -*-

from odoo import fields, models, api,_
from odoo.exceptions import UserError, ValidationError


# Sales module extension
class sale(models.Model):
    # """ Sales Module Extension """
    _inherit = 'sale.order'  # Seller
    # x_salesm = fields.Many2one('res.users', string='Salesman', related='partner_id.user_id')
    customer_reference = fields.Char(string='Custer_Reference', related='partner_id.customer_r')
    date_of_birth = fields.Date(string="Date Of Birth", required=False,related='partner_id.dob')
    mobile_number = fields.Integer(string="Mobile Number")
    email_id = fields.Char(string="Email")

    @api.onchange('partner_id')
    def _onchange_mobile_number(self):
        if self.partner_id:
            self.mobile_number=self.partner_id.mobile
            self.email_id=self.partner_id.email

    @api.constrains('payment_term_id', 'partner_id')
    def _check_payment_term(self):
        for rec in self:
            if rec.payment_term_id != rec.partner_id.property_supplier_payment_term_id:
                raise UserError('Payment Terms do not match!')

