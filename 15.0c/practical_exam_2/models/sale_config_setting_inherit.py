
from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    promotional_discount = fields.Boolean(string="Promotional Discount",
                                          implied_group='sale_management.group_sale_order_template')

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('practical_exam_2.promotional_discount',
                                                  self.promotional_discount)

        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        rec = self.env['ir.config_parameter'].sudo()
        res.update(
            promotional_discount=rec.get_param('practical_exam_2.promotional_discount'),
        )

        return res
