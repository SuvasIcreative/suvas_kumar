# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CollegeManagement(models.Model):
    _name = 'unv.course'
    # _inherit='res.partner'
    _description = 'unv.course'
    _rec_name = 'course_name'

    course_name = fields.Char(string='Course Name')
    course_code = fields.Integer()
    file = fields.Binary()
    student_enroll = fields.Integer(string="Student Enroll")

    # compute = '_compute_student_enroll'
    # def _compute_student_enroll(self):
    #     student_enroll = self.env['student.management'].search_count([('course', '=', self.ids)])
    #     self.student_enroll = student_enroll

    # def action_open_student_enroll(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Students',
    #         'res_model': 'student.management',
    #         'domain': [('course', '=', self.ids)],
    #         'view_mode': 'tree,form',
    #         'target': 'current',
    #
    #     }