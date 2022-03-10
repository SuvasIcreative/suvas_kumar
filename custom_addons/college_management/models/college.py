# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CollegeManagement(models.Model):
    _name = 'college.management'
    # _inherit='res.partner'
    _description = 'college.management'

    name = fields.Char(string="Name")
    address = fields.Text(string="Address")
    code = fields.Integer()
    email = fields.Char()
    course=fields.Selection([('course1', 'CIVIL ENGINEERING'), ('course2', 'COMPUTER ENGINEERING'),
                               ('course4', 'ELECTRICAL ENGINEERING '),
                               ('course3', 'ELECTRONICS & COMMUNICATION ENGINEERING'),
                               ('course5', ' MECHANICAL ENGINEERING'),
                               ('course6', 'AUTOMOBILE ENGINEERING '), ('course7', 'MECHANICAL ENGINEERING'),
                               ('course8', 'INFORMATION TECHNOLOGY ')], string='Course')
    rating=fields.Selection([('1','1'),('2','2'),('4','4'),('3','3')])



    # def send(self):
    #     print("funtion works")