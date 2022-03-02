# -*- coding: utf-8 -*-
'''This model is create to test defult_get,name_get and name_search'''
from odoo import models, fields, api
# from odoo.exceptions import UserError, ValidationError
# from datetime import datetime


class OrmPra(models.Model):
    _name = 'orm.pra'
    _description = 'orm.pra'

    name=fields.Many2one('rambo.rambo',string='Name')



    # @api.model
    # def default_get(self,field_list=[]):
    #     smart1=super(rambo, self).default_get(field_list)
    #     smart1['name']='Adrash'
    #     return smart1

