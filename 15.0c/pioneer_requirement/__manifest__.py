# -*- coding: utf-8 -*-
{
    'name': "Pioneer Requirement",

    'summary': """Pioneer Requirement""",

    'description': """Pioneer Requirement""",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'views/account_move_inherit_view.xml',
        'views/invoice_server_action_view.xml',

    ],
    # 'application': True,
    # 'auto_install': False,
    # 'description': '',
    'installable': True,
    'post_load': None,
    'version': '1.0',
    'web': False,
    'sequence': 10,
    'license': 'LGPL-3',

}