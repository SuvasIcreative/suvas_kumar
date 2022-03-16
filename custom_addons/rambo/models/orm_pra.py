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
    def action_read(self):
        read_list = self.env['res.partner'].search([])
        list1 = (read_list.read(['email', 'mobile']))
        for rec in list1:
            print(rec)


    def action_search_read(self):
        search_read_list=(self.env['res.partner'].search_read(domain=[('email','!=',False)],
                                                              fields={'email'}))
        for rec in search_read_list:
            print(rec)


    def action_browse(self):
        browse_list=self.env['res.partner'].browse([3,15,18,35])
        list2=(browse_list.read(['name','email', 'phone']))
        for rec in list2:
            print(rec)
