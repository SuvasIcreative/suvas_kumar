# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request


class WebsiteForm(http.Controller):

    @http.route(['/res_partner'], type='http', auth="user", website=True)
    def appointment(self):
        partners = request.env['res.partner'].sudo().search([])
        values = {}
        values.update({
           'partners': partners
        })
        return request.render("rental_management.tmp_customer_form", values)

    @http.route(['/customer/form/submit'], type='http', auth="public", website=True)
    def customer_form_submit(self, **post):
        print("\n\npppp\n\n")
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),

        })
        vals = {
            'partner': partner,
        }
        return request.render("rental_management.tmp_customer_form_success", vals)
