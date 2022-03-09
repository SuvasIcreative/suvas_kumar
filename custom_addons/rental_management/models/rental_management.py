# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from datetime import datetime

class RentalManagement(models.Model):
    _name = 'rental.management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'rental.management'

    name = fields.Char(string='Number', required=True, copy=False,
                       readonly=True, default=lambda self: _('New'))
    new_name_id = fields.Char(string="Name",required=True, tracking=True)
    customer_id = fields.Many2one('res.partner', string="Customer")
    rental_type_id=fields.Many2one('rental.type',string='Rental Type')
    start_date=fields.Datetime(string='Start Date',default=datetime.now(),readonly=True)
    end_date=fields.Datetime(string="End Date")
    # rental_product_id=fields.Many2one('product.template', string="Rental Product")
    rental_product_id = fields.Many2one(comodel_name="product.product", domain=[('is_rental', '=', True)])
    price=fields.Float(string='Price',related='rental_product_id.list_price',tracking=True)
    state=fields.Selection([('draft','Draft'),('waiting','Waiting'),
                            ('approve','Approve'),('cancel','Cancel')],string="state",tracking=True)


    @api.model
    def create(self, values):
        if values.get('name', _('New')) == _('New'):
            values['name'] = self.env['ir.sequence'].next_by_code('rental.management') or _('New')
        res = super(RentalManagement, self).create(values)
        return res

    _sql_constraints = [
        ('name_uniq', 'unique (new_name_id)', 'The name must be unique per person !')
    ]
