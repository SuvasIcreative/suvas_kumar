# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CollegeManagement(models.Model):
    _name = 'unv.course'
    # _inherit='res.partner'
    _description = 'unv.course'
    _rec_name = 'course_name'

    course_name = fields.Char(string='Course Name')
    course_code = fields.Integer()
    # file = fields.Binary()
    file = fields.Binary("Upload Company Logo (for Invoice)", attachment=True, store=True,
                         help="This field holds the image used for as companyLogo")
    student_enroll = fields.Integer(string="Student Enroll", compute='_compute_student_enroll')

    # compute = '_compute_student_enroll'
    def _compute_student_enroll(self):
        student_enroll = self.env['student.management'].search_count([('course_info_id', '=', self.ids)])
        self.student_enroll = student_enroll

    def action_open_student_enroll(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Students',
            'res_model': 'student.management',
            'domain': [('course_info_id', '=', self.ids)],
            'view_mode': 'tree,form',
            'target': 'current',
        }

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        """
        this is method is for
        search with customer email,name and phone number
        """
        args = args or []
        domain = []
        # print ("insideeeeeeeeeeeeeeeeeeeeeeeeeee", self._context)
        if self._context.get('suvas'):
            college = self.env['college.registration'].browse(self._context.get('suvas'))
            domain += [('id', 'in', college.available_course.ids)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)