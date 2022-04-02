# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CollegeOfManagement(models.Model):
    _name = 'department.management'
    _description = 'department.management'

    name = fields.Char(string="Name", required=True)



    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
