# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CollegeManagementWizard(models.TransientModel):
    _name = 'college.management.wizard'
    _description = 'college.management.wizard'

    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    enrollment_number = fields.Integer(string='Enrollment Number')
    address = fields.Text(string="Address")
    mobile_no = fields.Integer()
    email = fields.Char()
    course = fields.Char(string='Course')


    cancel = fields.Char()
    def college(self):
        print("Hello i am hear")
# address = fields.Text(string="Address")
    # code = fields.Integer()
    # email = fields.Char()

