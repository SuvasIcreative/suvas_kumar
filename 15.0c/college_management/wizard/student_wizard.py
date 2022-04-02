 # -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentManagementWizard(models.TransientModel):
    _name = 'student.management.wizard'
    _description = 'student.management'

    student_name = fields.Many2one('student.management',string='Student Name')
    enrollment_number = fields.Integer(string='Enrollment Number')
    description = fields.Text(string='Description')
    appointment_date = fields.Date(string='Appointment Date')
    appointment_time = fields.Selection([('1', '9am to 10am'),
                                       ('2', '10am to 11am'),
                                       ('3', '2pm to 3pm'),
                                       ('4', '3pm to 4pm')], string='Time', default='2')
