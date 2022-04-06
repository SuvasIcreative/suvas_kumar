# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import date, datetime


# Sales module extensions
class ResPartner(models.Model):
    # """ Sales Module Extension """
    _inherit = 'res.partner'

    date_of_birth = fields.Date(string="Date Of Birth", required=False)
    age = fields.Char(string="Age", compute="_set_age", store=True)

    @api.depends("date_of_birth")
    def _set_age(self):
        if self.date_of_birth:
            for record in self:
                today = date.today()
                age = datetime.strptime(str(record.date_of_birth), '%Y-%m-%d').date()
                record.age = today.year - age.year
                - ((today.month, today.day) < (age.month, age.day))
