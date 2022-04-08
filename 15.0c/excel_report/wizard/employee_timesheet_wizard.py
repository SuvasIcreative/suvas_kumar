# -*- coding: utf-8 -*-

from odoo import models, fields, api




class SaleOrderLineWizard(models.TransientModel):
    _name = 'employee.timeshit.wizard'
    _description = 'Create employee timeshit excel report '

    employee_ids = fields.Many2many(comodel_name='hr.employee', string="Employees")
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    def print_excel_report(self):
        print("haaa")