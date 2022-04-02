# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request

class Website(http.Controller):
    @http.route('/product', type='http', auth="user", website=True)
    def product_web(self, **data):
        contacts = request.env['product.template'].sudo().search([])
        return request.render(
            "rental_management.rental_web_page", {'product': contacts})

    @http.route(['/product/<model("product.template"):order>/'], type='http', auth="user", website=True)
    def product_templet_web(self, order=0, **data):
        print('****************************88', order)
        return http.request.render('rental_management.product_templet_web', {'order': order})
