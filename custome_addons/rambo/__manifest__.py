# -*- coding: utf-8 -*-
{
    'name': "rambo",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'contacts', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/sale_oder_wizard.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/sale.xml',
        'views/contact.xml',
        'views/smart_views.xml',
        'views/orm_pra.xml'
    ],
    'license': 'LGPL-3',
    'sequence': 10,
    'application': True,

}