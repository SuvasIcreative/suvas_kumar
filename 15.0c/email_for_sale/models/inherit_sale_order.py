# -*- coding: utf-8 -*-

from odoo import fields, models, api,_


class SaleOrder(models.Model):
    _inherit = 'sale.order'



    email = fields.Char(string="Email")

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        print("++++++++++++++++++++++++++++++++++++++++++******&^^&&")
        template_id = self.env.ref('email_for_sale.email_template_sale_order').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
