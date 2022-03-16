# -*- coding: utf-8 -*-

from odoo import fields, models,api


# Sales module extensions
class ResPartner(models.Model):
    # """ Sales Module Extension """
    _inherit = 'res.partner'

    dob = fields.Date(string="DOB", required=False)
    customer_r = fields.Char(string='Custer_Reference')

    # @api.model
    def name_get(self):
        """
        this method is for
        name of customer come with customer_reference
        """
        res = []
        for rec in self:
            res.append((rec.id, '%s -%s' % (rec.customer_r,rec.name)))
        return res


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
        return self._search(domain+args,limit=limit, access_rights_uid=name_get_uid)

    def search_mail(self):

        res_obj = self.search([])
        record_list = res_obj.read(['email', 'phone'])

        for rec in record_list:
            print(rec)
