""" This model is create for student page """
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StudentManagement(models.Model):
    """ This class is for student model this model is for student page"""
    _name = 'student.management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'student.management'

    name = fields.Char(string='Sr. Number', required=True, copy=False,
                       readonly=True, default=lambda self: _('New'))
    first_name = fields.Char(string="First Name", tracking=True)
    last_name = fields.Char(string="Last Name", tracking=True)
    image_1999 = fields.Image("Image", max_width=128, max_height=128)
    enrollment_number = fields.Integer(string='Enrollment Number', tracking=True)
    address = fields.Text(string="Address")
    mobile_no = fields.Integer()
    date_of_birth = fields.Date(string="Date_Of_Birth")
    email = fields.Char(tracking=True)
    college = fields.Many2one('college.registration', string='College')
    reference = fields.Many2one('res.partner', string="Reference")
    gender = fields.Selection([
        ('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender', tracking=True)
    course_id = fields.Many2many('unv.course', related='college.available_course')
    course_info_id = fields.Many2one('unv.course',string='Course')
    # yy = fields.Many2one('unv.course')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'),
                              ('complete', 'Complete'),
                              ('cancel', 'Cancel')],
                             string='status', default="draft", tracking=True)
    ''' This function change the state of form by clicking on confirm button '''
    def action_confirm(self):
        """ change the state of student form"""
        self.write({'state': 'confirm'})

    def action_draft(self):
        """ This function change the state of form by clicking on draft button """
        self.write({'state': 'draft'})

    def action_complete(self):
        """ This function change the state of form by clicking on complete button """
        self.write({'state': 'complete'})

    def action_cancel(self):
        """ This function change the state of form by clicking on cancel button """
        self.write({'state': 'cancel'})

    @api.model
    def create(self, values):
        """ First condition is for if in address field get None
        value then default get a string type of value

              and other one is for generate a sequence of form"""
        if not values.get('address'):
            values['address'] = 'Address.......'
        if values.get('name', _('New')) == _('New'):
            values['name'] = self.env['ir.sequence'].next_by_code('student.management') or _('New')
        res = super(StudentManagement, self).create(values)
        return res
