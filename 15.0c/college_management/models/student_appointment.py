 # -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentAppointment(models.Model):
    _name = 'student.appointment'
    _description = 'student.appointment'

    student_name = fields.Many2one('student.management',string='Student Name',required=True)
    enrollment_number = fields.Integer(related="student_name.enrollment_number",string='Enrollment Number')
    description = fields.Text(string='Description')
    appointment_date = fields.Date(string='Appointment Date')
    appointment_time = fields.Selection([('1', '9am to 10am'),
                                         ('2', '10am to 11am'),
                                         ('3', '2pm to 3pm'),
                                         ('4', '3pm to 4pm')], string='Time', default='2')

    def action_url(self):
        return {
            'type': 'ir.actions.act_url',
            'target':'new',
            'url':'https://www.youtube.com/watch?v=7jbaJSZLL8A'
            # 'url': self.env['iap.account'].get_credits_url(service_name='reveal'),
        }
        print("++++++++++++++++++++++++++++++")