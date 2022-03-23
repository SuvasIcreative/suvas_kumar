# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import date, datetime


# Sales module extensions
class ResPartner(models.Model):
    # """ Sales Module Extension """
    _inherit = 'res.partner'

    dob = fields.Date(string="Date Of Birth", required=False)
    age = fields.Char(string="Age", compute="_cal_age", store=True)
    customer_r = fields.Char(string='Custer Reference')


    # @api.model

    def name_get(self):
        """
        this method is for
        name of customer come with customer_reference
        """
        res = []

        # for rec in self:
        #     # if rec.customer_r:
        #     # if self.env['sale.order'].sudo().search_read(domain=[('partner_id', '=', 'partner_id')]):
        #     if self.env.context.get('customer_r','0'):
        #         res.append((rec.id, '%s -%s' % (rec.customer_r, rec.name)))
        #     else:
        #         res.append((rec.id, rec.name))
        #     return res

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        """
        this is method is for
        search with customer email,name and phone number
        """
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('email', operator, name), ('name', operator, name), ('phone', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

    def search_mail(self):

        res_obj = self.search([])
        record_list = res_obj.read(['email', 'phone'])

        for rec in record_list:
            print(rec)

    @api.depends("dob")
    def _cal_age(self):
        """ calculate age from given date of birth"""
        if self.dob:
            for record in self:
                today = date.today()
                age = datetime.strptime(str(record.dob), '%Y-%m-%d').date()
                record.age = today.year - age.year
                - ((today.month, today.day) < (age.month, age.day))

    # def name_get(self):
    #     result=[]
    #     for s in self:
    #         # if self.env['sale.order'].browse(self._context.get('partner_id')):
    #         #     print('+++++++++++++',self._context.get)
    #         name=s.name
    #         if s.customer_r:
    #             name+="({})".format(s.customer_r)
    #             result.append((s.id,name))
    #         else:
    #             result.append((s.id, s.name))
    #
    #     return result
    @api.depends('country_id')
    def name_get(self):
        res = []
        res=super(ResPartner, self).name_get()
        if self.env['sale.order']._context.get('special_display_name', False):
            for rec in self:
                if rec.country_id.name==False:
                    res.append((rec.id, '%s' % (rec.name)))
                else:
                    res.append((rec.id, '%s - %s' % (rec.country_id.name, rec.name)))
        else:
            for record in self:
                res.append([record.id, record.name])
        res = super(ResPartner, self).name_get()
        return res

    @api.depends('function')
    def name_get(self):
        result = []
        if self.env['student.management']._context.get('Nikhar', False):
            for rec in self:
                if rec.function == False:
                    result.append((rec.id, '%s' % (rec.name)))
                else:
                    result.append((rec.id, '%s - %s' % (rec.function, rec.name)))

        else:
            for record in self:
                result.append([record.id, record.name])
        # result=super(ResPartner, self).name_get()

        return result