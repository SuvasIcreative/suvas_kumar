# -*- coding: utf-8 -*-
from odoo.tools.misc import xlwt
import base64
from io import BytesIO
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning
from xlwt import easyxf



class SaleOrderLineWizard(models.TransientModel):
    _name = 'employee.timeshit.wizard'
    _description = 'Create employee timeshit excel report '

    employee_ids = fields.Many2many(comodel_name='hr.employee', string="Employees")
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    excel_file = fields.Binary(readonly=True)
    _sql_constraints = [
        ('check', 'CHECK((start_date <= end_date))', "End date must be greater then start date")
    ]
    def print_excel_report(self):
        if all([self.start_date, self.end_date]):
            analytic_line = self.env["account.analytic.line"]
            filename = 'Timesheet.xls'
            workbook = xlwt.Workbook(encoding="UTF-8")
            worksheet = workbook.add_sheet("Timesheet")
            header_style = easyxf('font:height 500; align: horiz center;font:bold True;')
            row1 = 2
            row2 = 3
            col1 = 1
            col2 = 5
            worksheet.write_merge(row1, row2, col1, col2, "Timesheet", header_style)
            worksheet.col(0).width = 3000

            header_line_style = easyxf('align: horiz center; font: bold True; \
                                borders: top_color black, bottom_color black, right_color black, \
                                    left_color black, left thin, right thin, top thin, bottom thin;')

            row = 5
            col = 1
            worksheet.write(row, col, 'Employee Name', header_line_style)
            worksheet.col(1).width = int(256 * 20)
            row = 5
            col = 2
            worksheet.write(row, col, 'Project', header_line_style)
            worksheet.col(2).width = int(256 * 23)
            row = 5
            col = 3
            worksheet.write(row, col, ' Task', header_line_style)
            worksheet.col(3).width = int(256 * 23)
            row = 5
            col = 4
            worksheet.write(row, col, 'Description', header_line_style)
            worksheet.col(4).width = int(256 * 20)
            row = 5
            col = 5
            worksheet.write(row, col, 'Hours', header_line_style)
            worksheet.col(5).width = int(256 * 20)
            cell = easyxf('borders: top_color black, bottom_color black, right_color black, \
                                left_color black, left thin, right thin, top thin, bottom thin;')
            total_hour = easyxf('align: horiz right; borders: top_color black, bottom_color black, right_color black, \
                                left_color black, left thin, right thin, top thin, bottom thin;')
            for employee_id in self.employee_ids:
                row += 1
                col = 1
                worksheet.write(row, col, employee_id.name, cell)
                employees_ids = analytic_line.search([('employee_id', '=', employee_id.id),
                                                     ('date', '>=', self.start_date),
                                                     ('date', '<=', self.end_date)])
                Row = row
                for project in employees_ids:
                    col = 2
                    worksheet.write(Row, col, project.project_id.name, cell)
                    Row += 1

                Row = row
                for task in employees_ids:
                    col = 3
                    worksheet.write(Row, col, task.task_id.name, cell)
                    Row += 1
                Row = row
                for description in employees_ids:
                    col = 4
                    worksheet.write(Row, col, description.name, cell)
                    Row += 1
                total_hours = 0
                Row = row
                for hours in employees_ids:
                    col = 5
                    worksheet.write(Row, col, hours.unit_amount, cell)
                    total_hours += hours.unit_amount
                    Row += 1
                worksheet.write_merge(Row, Row, col1, col2, "Total Hours: {}".format(total_hours), total_hour)
                row = Row + 1
            fp = BytesIO()
            workbook.save(fp)
            fp.seek(0)
            excel_file = base64.encodebytes(fp.getvalue())
            fp.close()
            self.write({'excel_file': excel_file})

            url = ('web/content/?model=employee.timeshit.wizard&download=true&field=excel_file&id=%s&filename=%s'
                   % (self.id, filename))
            if self.excel_file:
                return {'type': 'ir.actions.act_url',
                        'url': url,
                        'target': 'new'
                        }
        else:
            raise ValidationError("Enter Date..!")
