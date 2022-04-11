# -*- coding: utf-8 -*-
{
    'name': "Mail For Sale",

    'summary': """create this model for send mail from sale order""",

    'description': """Create for send mail """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/inherit_sale_order.xml'
    ],
    # 'application': True,
    # 'auto_install': False,
    'installable': True,
    'post_load': None,
    'version': '1.0',
    'web': False,
    'sequence': 10,
    'license': 'LGPL-3',

}
