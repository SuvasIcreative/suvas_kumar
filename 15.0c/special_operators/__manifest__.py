# -*- coding: utf-8 -*-
{
    'name': "Special Operator",

    'summary': """Special Operator""",

    'description': """Special Operator software""",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['mail','sale'],

    # always loaded
    'data': [
        'wizard/wizard1.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
    ],
    'version': '1.0',
    'web': False,
    'license': 'LGPL-3',

}
