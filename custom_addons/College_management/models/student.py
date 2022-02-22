# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class StudentManagement(models.Model):
    _name = 'student.management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'student.management'

    name = fields.Char(string='Sr. Number', required=True, copy=False,
                       readonly=True, default=lambda self: _('New'))
    first_name = fields.Char(string="First Name",tracking=True)
    last_name = fields.Char(string="Last Name",tracking=True)
    enrollment_number = fields.Integer(string='Enrollment Number',tracking=True)
    address = fields.Text(string="Address")
    mobile_no = fields.Integer()
    email = fields.Char(tracking=True)
    course = fields.Char(string='Course', tracking=True)
    reference = fields.Many2one('res.partner', string="Reference")
    gender = fields.Selection([
        ('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender',
         tracking=True)

    state = fields.Selection([
        ('draft', 'Draft'), ('confirm', 'Confirm'), ('complete', 'Complete'), ('cancel', 'Cancel')], string='status',
        default="draft", tracking=True)

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

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

