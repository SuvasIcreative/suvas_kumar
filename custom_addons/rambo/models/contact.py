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
        res = []
        for rec in self:
            res.append((rec.id, '%s -%s' % (rec.name,rec.customer_r)))
        return res


    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('email', operator, name), ('name', operator, name), ('phone', operator, name)]
        return self._search(domain, args, limit=limit, access_rights_uid=name_get_uid)