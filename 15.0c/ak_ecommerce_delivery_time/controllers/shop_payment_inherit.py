# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteDeliveryTime(WebsiteSale):
    """Add Customer Delivery time slot,
    commentfunctions to the website_sale controller."""
    @http.route('/shop/payment', type='http', auth='public', website=True, sitemap=False)
    def shop_payment(self, **post):
        """
        This function to get expect_time_slot for delivery
        """
        res = super(WebsiteDeliveryTime, self).shop_payment(**post)
        timeshit = request.env['delivery.time.slots'].sudo().search([('state', '=', 'active')])
        time_list = []
        for delivery_time in timeshit:
            state_values = (dict(delivery_time._fields['time_slot'].selection)
                            .get(delivery_time.time_slot))
            time_list.append(state_values)
        res.qcontext.update({'timeshit': time_list})
        return res

class WebsiteSaleDelivery(WebsiteSale):


    """Add Customer Delivery time slot, Delivery date and delivery functions
     to the website_sale controller."""
    @http.route(['/shop/customer_order_delivery'], type='json', auth="public",
                methods=['POST'], website=True)
    def customer_delivery(self, **post):
        """ Json method that used to add a delivery date and/or comment
        and/or expect_time_slot when the user clicks on 'pay now' button.
        """
        if post.get('delivery_date') or post.get('delivery_comment'):
            order = request.website.sale_get_order().sudo()
            redirection = self.checkout_redirection(order)
            if redirection:
                return redirection

            if order and order.id:
                values = {}
                if post.get('delivery_comment'):
                    values.update(
                        {'customer_comment': post.get('delivery_comment')})
                else:
                    values.update(
                        {'customer_comment': 'No Comment'})
                p_date = datetime.strptime(post.get('delivery_date'), '%m/%d/%Y')

                if order and order.id:
                    values.update({
                        'commitment_date': p_date
                    })

                if post.get('delivery_time'):
                    values.update(
                        {'expect_time_slot': post.get('delivery_time')})
                order.write(values)
        return True
