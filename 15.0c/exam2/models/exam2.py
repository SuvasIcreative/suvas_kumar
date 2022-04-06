# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Exam(models.Model):
    _name = 'exam.exam'
    _description = 'exam.exam'

    name = fields.Char()
