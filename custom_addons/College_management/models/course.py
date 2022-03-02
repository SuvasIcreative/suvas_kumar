# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CollegeManagement(models.Model):
    _name = 'unv.course'
    # _inherit='res.partner'
    _description = 'unv.course'

    # college_name=fields.Many2one()
    course_name = fields.Selection([('course1', 'CIVIL ENGINEERING'), ('course2', 'COMPUTER ENGINEERING'),
                               ('course4', 'ELECTRICAL ENGINEERING '),
                               ('course3', 'ELECTRONICS & COMMUNICATION ENGINEERING'),
                               ('course5', ' MECHANICAL ENGINEERING'),
                               ('course6', 'AUTOMOBILE ENGINEERING '), ('course7', 'MECHANICAL ENGINEERING'),
                               ('course8', 'INFORMATION TECHNOLOGY ')], string='Course')
    course_code = fields.Integer()
