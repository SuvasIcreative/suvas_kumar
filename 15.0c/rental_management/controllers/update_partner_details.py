# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request



class WebsiteForm(http.Controller):

    @http.route('/partner', type='http', auth="user", website=True)
    def appointment(self):
        partners = request.env['res.partner'].sudo().search([])
        return request.render("rental_management.update_partner_form", {'partners': partners})

    @http.route(['/partner/details/'], type='http', auth="public", website=True)
    def customer_form_submit(self, **post):
        partner = request.env['res.partner'].browse(eval(post.get('partner_id')))
        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])
        return request.render("rental_management.partner_form_success", {'partners': partner,
                                                                         'countries': countries,
                                                                         'states': states})

    @http.route(['/updated/details'], type='http', auth="public", website=True)
    def partner_detail_update_submit(self, **post):
        print("\n\npppp\n\n", post)
        print('\n\n\n',post.get('partner_id'),'\n\n\n',)
        partner = request.env['res.partner'].search([('id', '=', post.get('partner_id'))]).write({
            'name': post.get('name'),
            'street2': post.get('street2'),
            'state_id': eval(post.get('state_id')),
            'country_id': eval(post.get('country_id')),
            'city': post.get('city'),
            'email': post.get('email'),
            'phone': post.get('phone')

        })
        vals = {
            'partner': partner,
        }
        print(partner)
        return request.render("rental_management.tmp_partner_form_success", vals)
