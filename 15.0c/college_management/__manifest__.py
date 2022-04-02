# -*- coding: utf-8 -*-




{
    'name': "College Management",

    'summary': """College Management software""",

    'description': """College Management software""",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/college.xml',
        'views/department.xml',
        'views/student.xml',
        'wizard/student_wizard.xml',
        'wizard/college_wizard.xml',
        'views/college_registration.xml',
        'views/course.xml',
        'views/i_res_config_settings.xml',
        'views/student_appointment.xml',
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
