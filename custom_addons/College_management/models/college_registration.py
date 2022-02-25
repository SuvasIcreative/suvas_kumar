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
    rating = fields.Selection([('1','1'),('2','2'),('4','4'),('3','3')])
    #

    # def send(self):
    #     print("funtion works")