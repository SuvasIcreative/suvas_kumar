# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class rambo(models.Model):
    _name = 'smart.model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _description = 'smart.model'

    name = fields.Char(String="Name", tracking=True)
    mobile_number = fields.Char(string="Mobile Number")
    age=fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    dob = fields.Date(string="DOB", tracking=True)
    bool = fields.Boolean()
    email=fields.Char(string="Email")
    active = fields.Boolean(string="Active", default=True)
    notes = fields.Html(string='Terms and Conditions')
    create_date = fields.Datetime(readonly=True)
    file = fields.Binary()
    gender = fields.Selection([('a', 'Male'), ('b', 'Female'), ('c', 'Other')], string="Gender", tracking=True)
    refer = fields.Reference(selection=[('res.partner', 'From contact'), ('sale.order', 'Sale list'),
                                        ('account.move', 'Invoicing'), ('product.template', 'Inventory Product')])
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
        if self.name in ('sam', 'radhe', 'make'):
            raise UserError('This name is blocked all ready')

    # class Demo(models.Model):
    #     _inherit = 'res.partner'
    #     res_id = fields.Many2one('rambo.rambo')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

    def action_confirm(self):
        display_mas = """Confirm"""
        self.message_post(body=display_mas)

    @api.constrains('mobile_number')
    def _check_phone_number(self):

        for rec in self:
            if rec.mobile_number and not len(rec.mobile_number) == 10:
                raise ValidationError(_("Enter valid details..... "))
        return True

    def action_search(self):
        for rec in self:
            male=self.env['smart.model'].search(['|',('gender','=','a'),('age','>=','20')])
            print("this is search of male...",male)
            female=self.env['smart.model'].search([('gender','=','b'),('age','>=','20')])
            print("this is search of male...",female)

            smart = self.env['smart.model'].search_count([('gender','=','b'),('age','>=','20')])
            print("this is search of male...", smart)

            smart_dud=self.env.ref('rambo.smart_kanban_action_window')
            print(smart_dud)

            smart_dud1 = self.env['smart.model'].browse([1,2,5,20])
            print(smart_dud1)
            hry=self.browse([5])
            print(hry)


            new_record = self.copy()
            print(new_record)
    #
    def action_confirm(self):
    #      # self.create({'name': 'Cybrosys', 'email': 'demo@cybrosys.com'})
    #
    #     self.unlink()
    #
        self.write({'email': 'demo@cybrosys.info12305'})
    #
    #     man=self.browse([12])
    #     if man.exists():
    #         print("The record has been deleted")
    #     else:
    #         print("56859852")


    @api.model
    def default_get(self,field_list=[]):
        smart1=super(rambo, self).default_get(field_list)
        smart1['name']='Adrash'
        return smart1

