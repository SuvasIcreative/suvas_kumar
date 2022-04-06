# -*- coding: utf-8 -*-
{
    'name': "Exam 2",

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
    'depends': ['sale', 'contacts'],

    # always loaded
    'data': [
        'wizard/exam2_wizard.xml',
        'wizard/wizard_exam_f1.xml',
        'views/exam2.xml',
        'views/res_config_set.xml',
        'views/res_partner.xml',

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