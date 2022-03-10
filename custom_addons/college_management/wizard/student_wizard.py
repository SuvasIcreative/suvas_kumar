 # -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentManagementWizard(models.TransientModel):
    _name = 'student.management.wizard'
    _description = 'student.management'

    # first_name = fields.Char(string="First Name")
    # last_name = fields.Char(string="Last Name")
    # enrollment_number = fields.Integer(string='Enrollment Number')
    # address = fields.Text(string="Address")
    # mobile_no = fields.Integer()
    # email = fields.Char()
    # course = fields.Char(string='Course')
    # send=fields.Char()
    procure_calculation=fields.Char()
    cancel=fields.Char()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
