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



    def name_get(self):
        """ Utility method to allow name_get to be overrided without re-browse the partner """
        result = super(ResPartner, self).name_get()
        for rec, get_name in zip(self,result):
            if rec.country_id and self.env.context.get('special_display_name') == 'country_name':
                print('_hkjjjjjjjjjjhsdfhuishuifyhshfgisduih___')
                index = result.index(get_name)
                result[index] = (rec.id, f"[{rec.country_id.name}] and {rec.name}")
            if rec.customer_r and self.env.context.get('com_ref') == 'customer_h':
                print('____________________________')
                index = result.index(get_name)
                result[index] = (rec.id, f"[{rec.customer_r}] and {rec.name}")
        return result
        # return [(rec.id, '%s-%s' % (
        #     rec.name, rec.country_id and rec.country_id.code or '')) for rec in self]
        # if self.env['student.management']._context.get('Nikhar', False):
        #     for rec in self:
        #         if rec.function == False:
        #             result.append((rec.id, '%s' % (rec.name)))
        #         else:
        #             result.append((rec.id, '%s - %s' % (rec.function, rec.name)))

        # for rec in self:
        #     if self._context.get('special_display_name', False) and rec.country_id:
        #         result.append((rec.id, '%s - %s' % (rec.country_id.name, rec.name)))
        #         return result
        #     else:
        #         super(ResPartner, rec).name_get()