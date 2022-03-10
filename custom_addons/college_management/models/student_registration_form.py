# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StudentRegistrationForm(models.Model):
    _name = 'student.registration.form'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'student.registration.form'

    # name = fields.Char(string='Sr. Number', required=True, copy=False,
    #                    readonly=True, default=lambda self: _('New'))
    student_id=fields.Integer(string='Sudent ID')
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    # enrollment_number = fields.Integer(string='Enrollment Number', tracking=True)
    address = fields.Text(string="Address")
    mobile_no = fields.Integer()
    date_of_birth = fields.Date(string="Date_Of_Birth")
    email = fields.Char()
    college = fields.Many2one('college.registration')
    # student_count = fields.Integer(string='Student Count',compute='_compute_student_count')
    # college = fields.Selection([('college1', 'VISHWAKARMA GOVERNMENT ENGINEERING COLLEGE'),
    #                             ('college2', 'BIRLA VISHVAKARMA MAHAVIDHYALAYA'),
    #                             ('college3', 'RAKSHA SHAKTI UNIVERSITY'),
    #                             ('college4', 'GUJARAT POWER ENGINEERING AND RESEARCH INSTITUTE'),
    #                             ('college5', 'AHMEDABAD INSTITUTE OF TECHNOLOGY'),
    #                             ('college6', 'ALPHA COLLEGE OF ENGINEERING & TECHNOLOGY'),
    #                             ('college7', 'APOLLO INSTITUTE OF ENGINEERING & TECHNOLOGY'),
    #                             ('college8', 'SAL COLLEGE OF ENGINEERING'),
    #                             ('college9', 'SAL ENGINEERING & TECHNICAL INSTITUTE'),
    #                             ('college10', 'SAL INSTITUTE OF TECHNOLOGY & ENGINEERING RESEARCH'),
    #                             ('college11', 'OM ENGINEERING COLLEGE'),
    #                             ('college12', 'PRIME INSTITUTE OF ENGINEERING & TECHNOLOGY')], string='College',
    #                            tracking=True)
    reference = fields.Many2one('res.partner', string="Reference")
    gender = fields.Selection([
        ('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender', tracking=True)
    course = fields.Selection([('course1', 'CIVIL ENGINEERING'), ('course2', 'COMPUTER ENGINEERING'),
                               ('course4', 'ELECTRICAL ENGINEERING '),
                               ('course3', 'ELECTRONICS & COMMUNICATION ENGINEERING'),
                               ('course5', ' MECHANICAL ENGINEERING'),
                               ('course6', 'AUTOMOBILE ENGINEERING '), ('course7', 'MECHANICAL ENGINEERING'),
                               ('course8', 'INFORMATION TECHNOLOGY ')], string='Course', tracking=True)


