 # -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentManagementWizard(models.TransientModel):
    _name = 'student.management.wizard'
    _description = 'student.management'

    student_name = fields.Many2one('student.management',string='Student Name')
    enrollment_number = fields.Integer(string='Enrollment Number')

    # procure_calculation=fields.Char()
    # cancel=fields.Char()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
