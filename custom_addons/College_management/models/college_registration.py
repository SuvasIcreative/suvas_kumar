# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CollegeRegistration(models.Model):
    _name = 'college.registration'
    # _inherit='res.partner'
    _description = 'college.registration'

    name = fields.Char(string="Name")
    address = fields.Text(string="Address")
    code = fields.Integer()
    email = fields.Char()
    available_course=fields.Many2many('unv.course',string='Courses')
    rating = fields.Selection([('1','1'),('2','2'),('4','4'),('3','3')])
    student_count = fields.Integer(string='Student Count',compute='_compute_student_count')
    # course_count = fields.Integer(string='Number of Course Available',compute='_compute_course_count')

    def _compute_student_count(self):

        student_count = self.env['student.management'].search_count([('college', '=', self.ids)])
        self.student_count = student_count


    def action_open_available_student(self):
        return {
            'type':'ir.actions.act_window',
            'name':'Students',
            'res_model':'student.management',
            'domain':[('college','=',self.ids)],
            'view_mode':'tree,form',
            'target':'current',

        }
    # def _compute_course_count(self):
    #     course_count = self.env['college.registration'].search_count([('course_name', '=', self.ids)])
    #     self.student_count = course_count

    # def send(self):
    #     print("funtion works")