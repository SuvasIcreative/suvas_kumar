# -*- coding: utf-8 -*-
{
    'name': "Rental Management",

    'summary': """Rental Management software""",

    'description': """Rental Management software""",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'sale', 'contacts'],

    # always loaded
    'data': [
        'data/data.xml',
        'data/rec_partner_category_data.xml',
        'data/mail_template.xml',
        'security/ir.model.access.csv',
        'wizard/wizard1.xml',
        'views/rental_template_web.xml',
        'views/rental_management.xml',
        'views/rental_type.xml',
        'views/product_template.xml',
        'report/rental_paper_format.xml',
        'report/rental_management_template.xml',
        'report/rental_management_action.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',

    ],
    'application': True,
    'auto_install': False,
    'description': '',
    'installable': True,
    'post_load': None,
    'version': '1.0',
    'web': False,
    'sequence': 10,
    'license': 'LGPL-3',

}
