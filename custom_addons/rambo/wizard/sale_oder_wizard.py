#
#
#  # -*- coding: utf-8 -*-
#
from odoo import models, fields, api
#
#
class SaleOderWizard(models.TransientModel):
    _name = 'sale.wizard'
    _description = 'sale.wizard'


    customer_id = fields.Many2one('res.partner',string="Customer")
    sale_person = fields.Char(string="Sales Person")
    sale_person_contact = fields.Char(string="Sales Person Contact")
    payment_term = fields.Char(string="Payment Terms")
    customer_email_id = fields.Char(string=' Customer Email')

    # @api.onchange('customer_id')
    # def _onchange_phone_number(self):
    #     if self.customer_id:
    #         self.payment_term = self.customer_id.property_supplier_payment_term_id.name
    #         self.sale_person_contact = self.customer_id.phone
    #         self.sale_person_id = self.customer_id.user_id.name
    #         self.customer_email_id = self.customer_id.email


    @api.model
    def default_get(self, fields_list):
        sale_rec = self.env["sale.order"]
        active_id = self.env.context.get('active_id')
        rec = sale_rec.browse(int(active_id))
        val = rec.read(['partner_id','email_id','user_id','payment_term_id','mobile_number'])
        SaleOrder = super(SaleOderWizard, self).default_get(fields_list)

        # print("\n\n\n\n",SaleOrder,"\n\n",val,"\n\n\n\n")
        for r in val:
            name = (r["partner_id"])
            sale_person = reversed(r["user_id"])
            SaleOrder['customer_id'] = tuple(name)[0]
            SaleOrder['customer_email_id'] = r["email_id"]
            SaleOrder['sale_person'] = tuple(sale_person)[0]
            SaleOrder['payment_term'] = r["payment_term_id"]
            SaleOrder['sale_person_contact'] = r["mobile_number"]
            return SaleOrder

