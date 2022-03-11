

 # -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOderWizard(models.TransientModel):
    _name = 'sale.wizard'
    _description = 'sale.wizard'


    customer_id = fields.Many2one('res.partner',string="Customer")
    sale_person_id = fields.Char(string="Sales Person")
    sale_person_contact = fields.Char(string="Sales Person Contact")
    payment_term = fields.Char(string="Payment Terms")
    customer_email_id = fields.Char(string=' Customer Email')

    @api.onchange('customer_id')
    def _onchange_phone_number(self):
        if self.customer_id:
            self.payment_term = self.customer_id.property_supplier_payment_term_id.name
            self.sale_person_contact = self.customer_id.phone
            self.sale_person_id = self.customer_id.user_id.name
            self.customer_email_id = self.customer_id.email



