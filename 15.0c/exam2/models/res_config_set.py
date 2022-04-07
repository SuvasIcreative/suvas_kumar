
from odoo import fields, models, api
from datetime import date, datetime



class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    module_crm = fields.Boolean(string='CRM')
    current_month_sale_oder_ids = fields.Many2many('sale.order',
                                                   string="this Month Oder",
                                                   domain=[('date_order', '>=',
                                                           datetime(datetime.today().year,
                                                                    datetime.today().month, 1)),
                                                           ('date_order', '<',
                                                           datetime(datetime.today().year,
                                                                    datetime.today().month+1, 1))])

    @api.model
    def get_values(self):
        rec = super(ResConfigSetting, self).get_values()
        orders = self.env['ir.config_parameter'].get_param('exam2.current_month_sale_oder_ids')
        if orders:
            rec.update(
                current_month_sale_oder_ids=[(6, 0, eval(orders))]
            )
        return rec

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param('exam2.current_month_sale_oder_ids',
                                                  self.current_month_sale_oder_ids.ids)
        super(ResConfigSetting, self).set_values()
