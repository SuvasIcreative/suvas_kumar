# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StudentManagement(models.Model):
    _name = 'student.management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'student.management'

    name = fields.Char(string='Sr. Number', required=True, copy=False,
                       readonly=True, default=lambda self: _('New'))
    first_name = fields.Char(string="First Name", tracking=True)
    last_name = fields.Char(string="Last Name", tracking=True)
    enrollment_number = fields.Integer(string='Enrollment Number', tracking=True)
    address = fields.Text(string="Address")
    mobile_no = fields.Integer()
    date_of_birth = fields.Date(string="Date_Of_Birth")
    email = fields.Char(tracking=True)
    college = fields.Many2one('college.registration', string='College')
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

    state = fields.Selection([
        ('draft', 'Draft'), ('confirm', 'Confirm'), ('complete', 'Complete'), ('cancel', 'Cancel')], string='status',
        default="draft", tracking=True)



    # @ api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

    # def send(self):
    #     print("Funtion Work")
    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_draft(self):
        self.write({'state': 'draft'})

    def action_complete(self):
        self.write({'state': 'complete'})

    def action_cancel(self):
        self.write({'state': 'cancel'})

    @api.model
    def create(self, values):
        if not values.get('address'):
            values['address'] = 'Address.......'
        if values.get('name', _('New')) == _('New'):
            values['name'] = self.env['ir.sequence'].next_by_code('student.management') or _('New')
        res = super(StudentManagement, self).create(values)
        return res
