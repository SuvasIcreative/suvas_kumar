# -*- coding: utf-8 -*-
{
    'name': "Customer Delivery",

    'summary': """ Customer Delivery""",

    'description': """Customer Delivery""",

    'author': "Suvas Kumar",
    'website': "www.aktivsoftware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['website', 'website_sale', 'sale_management', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_time_slots_view.xml',
        'views/shop_payment_web_inherit.xml',
        'views/sale_order_inherit_view.xml',
        'views/stock_picking_inherit_view.xml',
        'report/report_stockpicking_operations_inherit.xml',
    ],
    'assets': {
                'web.assets_frontend': [
                    'ak_ecommerce_delivery_time/static/src/js/website_customer_order_delivery.js'
                ],
            },
    'application': True,
    'auto_install': False,
    'installable': True,
    'post_load': None,
    'version': '15.0.1.0.0',
    'web': False,
    'sequence': 10,
    'license': 'LGPL-3',


}
