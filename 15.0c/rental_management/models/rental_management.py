# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import UserError, ValidationError
from random import randrange
from random import randint
import random
import string




class RentalManagement(models.Model):
    _name = 'rental.management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'rental.management'

    name = fields.Char(string='Number', required=True, copy=False,
                       readonly=True, default=lambda self: _('New'))
    new_name_id = fields.Char(string="Name", required=True, tracking=True)
    customer_id = fields.Many2one('res.partner', string="Customer")
    rental_type_id = fields.Many2one('rental.type', string='Rental Type')
    start_date = fields.Datetime(string='Start Date', default=datetime.now(), readonly=True)
    end_date = fields.Datetime(string="End Date", required=True)
    rental_product_id = fields.Many2one(comodel_name="product.product", domain=[('is_rental', '=', True)])
    currency_id = fields.Many2one("res.currency", string="Currency", default=20, readonly=True)
    price = fields.Float(string='Price', related='rental_product_id.list_price', tracking=True)
    rental_user_id = fields.Many2one('res.users', string='Email sent')
    email_id = fields.Char(string='Email')
    random_code = fields.Char(readonly=True)
    state = fields.Selection([('draft', 'Draft'), ('waiting', 'Waiting'),
                             ('approve', 'Approve'), ('cancel', 'Cancel')], string="state", tracking=True)


    @api.model
    def create(self, values):
        if values.get('name', _('New')) == _('New'):
            values['name'] = self.env['ir.sequence'].next_by_code('rental.management') or _('New')
        res = super(RentalManagement, self).create(values)
        return res

    _sql_constraints = [
        ('name_uniq', 'unique (new_name_id)', 'The name must be unique per person !')
    ]

    @api.constrains('end_date', 'start_date')
    def date_constrains(self):
        for rec in self:
            if rec.end_date < rec.start_date:
                raise ValidationError(_('Sorry, End Date Must be greater Than Start Date...'))


    def action_send_email(self):
        print("++++++++++++++++++++++++++++++++++++++++++******&^^&&")
        template_id = self.env.ref('rental_management.email_template_rental_management').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)


    def generate_cord(self):
        self.write({'random_code': (''.join(
            random.SystemRandom().choice(string.ascii_uppercase) for _ in range(randint(5, 5))))+''+'-M'})

































    # def generate_record_name(self):
    #     # Generates a random name between 9 and 15 characters long and writes it to the record.
    #     self.write({'name': ''.join(
    #         random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9, 15)))})