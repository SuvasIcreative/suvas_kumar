# -*- coding: utf-8 -*-
{
    'name': "Practical Exam 2",

    'summary': """Practical Exam 2""",

    'description': """Practical Exam 2""",

    'author': "Suvas",
    'website': "http://www.aktivsoftware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'contacts', 'sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/sale_security_inherit.xml',
        'data/product_category_data.xml',
        # 'data/mail_template_data.xml',
        'views/sale_config_setting_inherit_view.xml',
        'views/sale_order_inherit_view.xml',
        'views/promotional_discount_view.xml',

    ],
    'application': True,
    'auto_install': False,
    'installable': True,
    'post_load': None,
    'web': False,
    'sequence': 10,
    'license': 'LGPL-3',

}
