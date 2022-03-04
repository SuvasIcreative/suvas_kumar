# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime


class rambo(models.Model):
    _name = 'rambo.rambo'
    _description = 'rambo.rambo'
    _rec_name = 'name'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    dob = fields.Date(string="DOB")
    bool = fields.Boolean()
    active = fields.Boolean(string="Active", default=True)
    notes = fields.Html(string='Terms and Conditions')
    create_date = fields.Datetime(readonly=True)
    file = fields.Binary()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    refer = fields.Reference(selection=[('res.partner', 'From contact'), ('sale.order', 'Sale list'),
                                        ('account.move', 'Invoicing'), ('product.template', 'Inventory Product')])
    user = fields.Many2one('res.users')
    user1 = fields.Many2one(comodel_name='res.users', delegate=False)
    mod_ids = fields.One2many('res.partner', 'res_id', string='Costumer')
    mod_ids1 = fields.Many2many(comodel_name='res.partner',
                                relation='table_name',
                                column1='col_name',
                                column2='other_col_name')

    _sql_constraints = [
        ('name_dob_uniq', 'unique (name,dob)', 'The name/date of birth must be unique per person !')
    ]

    @api.constrains('name')
    def _constrains_reconcile(self):
        for rambo.rambo in self:
            if self.name in ('sam', 'radhe', 'make'):
                raise UserError('This name is blocked all ready')

    '''search name with gender'''

    @api.model
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s -%s' % (rec.name, rec.gender)))
        return res

    '''Hear this function is create for orm field relation many2one in that 
     search data use by user filed data,name,and gender this give us output  '''

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('user', operator, name), ('name', operator, name), ('gender', operator, name)]
        return self._search(domain, args, limit=limit, access_rights_uid=name_get_uid)


''' For one2many field inherit'''
class Demo(models.Model):
    _inherit = 'res.partner'
    res_id = fields.Many2one('rambo.rambo')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
