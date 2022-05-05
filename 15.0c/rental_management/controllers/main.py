# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers import portal

class Website(http.Controller):
    @http.route('/product', type='http', auth="user", website=True)
    def product_web(self, **data):
        contacts = request.env['product.template'].sudo().search([])
        return request.render(
            "rental_management.rental_web_page", {'product': contacts})

    @http.route(['/product/<model("product.template"):order>/'], type='http', auth="user", website=True)
    def product_templet_web(self, order=0, **data):
        # print('****************************88', order)
        return http.request.render('rental_management.product_templet_web', {'order': order})



class WebsiteForm(http.Controller):

    @http.route(['/rental_form'], type='http', auth="public", website=True)
    def partner_form(self, **post):
        print("\n\nhello\n\n")
        partners = request.env['res.partner'].sudo().search([])
        values = {}
        values.update({
            'partners': partners
        })
        products = request.env['product.product'].sudo().search([])
        value = {}
        values.update({
            'products': products
        })
        return request.render("rental_management.online_appointment_form", values, value)

    @http.route(['/rental_form/submit'], type='http', auth="public", website=True)
    def customer_form_submit(self, **post):
        print("\n\npppp\n\n")
        partner = request.env['rental.management'].create({
            'new_name_id': post.get('name'),
            'email_id': post.get('email'),
            'end_date': post.get('end_date'),
            'customer_id': post.get('customer_id'),
            'rental_product_id': post.get('rental_product_id')

        })
        vals = {
            'partner': partner,
        }
        return request.render("rental_management.tmp_customer_form_success", vals)


class CustomerPortal(portal.CustomerPortal):


    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        values["abc"] = request.env["rental.management"].search_count([('state', '=', 'waiting')])
        # partner = request.env.user.partner_id
        #
        # SaleOrder = request.env['sale.order']
        # if 'quotation_count' in counters:
        #     values['quotation_count'] = SaleOrder.search_count(self._prepare_quotations_domain(partner)) \
        #         if SaleOrder.check_access_rights('read', raise_exception=False) else 0
        # if 'order_count' in counters:
        #     values['order_count'] = SaleOrder.search_count(self._prepare_orders_domain(partner)) \
        #         if SaleOrder.check_access_rights('read', raise_exception=False) else 0

        return values





# config_parameter="exam2.current_month_sale_oder_ids"