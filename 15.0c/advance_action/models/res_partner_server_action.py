from odoo import models, fields, api

class ConfirmSale(models.Model):
    _inherit = "res.partner"



    def action_update_some_field(self):
        self.write({'name': 'selmon boi', 'phone': '910639255', 'email': 'semon@1235', 'mobile': '54679777734'})

    def create_record(self):
        value=({'name': 'selm', 'phone': '910639255', 'email': 'semon@1235',
                'mobile': '54679777734','customer_rank':10})
        self.env['res.partner'].create(value)




class SaleScheduled(models.Model):
    _inherit = "sale.order"


    # def demo_action(self):
    #     rec = self.search([('state', 'in', ['draft', 'sent'])])
    #     print("\n\n", rec,"\n\n")
    #     rec.action_confirm()
    @api.model
    def demo_action(self):
        print("----------------------------------------------------------")
        for rec in self.search([('state', '=', 'draft')]):

            rec.write({'state': 'sale'})





