# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime



class rambo(models.Model):
    _name = 'smart.model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _description = 'smart.model'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    dob = fields.Date(string="DOB", tracking=True)
    bool = fields.Boolean()
    active = fields.Boolean(string="Active", default=True)
    notes = fields.Html(string='Terms and Conditions')
    create_date = fields.Datetime(readonly=True)
    file = fields.Binary()
    gender = fields.Selection([('a', 'Male'),('b', 'Female'),('c', 'Other')],string="Gender")
    refer = fields.Reference(selection=[('res.partner', 'From contact'),('sale.order', 'Sale list'),
                                        ('account.move', 'Invoicing'),('product.template', 'Inventory Product')])
    user = fields.Many2one('res.users')
    user1 = fields.Many2one(comodel_name='res.users', delegate=False)
    # mod_ids = fields.One2many('res.partner', 'res_id', string='Costumer')
    # mod_ids1 = fields.Many2many(comodel_name='res.partner',
    #                            relation='table_name',
    #                            column1='col_name',
    #                            column2='other_col_name')

    _sql_constraints = [
        ('name_dob_uniq', 'unique (name,dob)', 'The name/date of birth must be unique per person !')
    ]

    @api.constrains('name')
    def _constrains_reconcile(self):
        if self.name in ('sam','radhe','make'):
            raise UserError('This name is blocked all ready')



# class Demo(models.Model):
#     _inherit = 'res.partner'
#     res_id = fields.Many2one('rambo.rambo')



    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
