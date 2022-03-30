# -*- coding: utf-8 -*-
{
    'name': "Confirm Sale",

    'summary': """
        Inherit Sale Order and override Confirm Sale button.
        Add new fields on the partner called Age(In years) and Birth Date.""",

    'description': """
        Inherit Sale Order and override Confirm Sale button. You need to raise UserError before confirming the sale order if the order line count is greater than 3.
UserError: You can only add max 3 lines per order.
        Add new fields on the partner called Age(In years) and Birth Date. 
-> Birth Date: type Date - User will manually add value to this field.
-> Age(In years): type Integer - Compute field it will automatically calculate the number of years till now based on Birthdate. (FYI: here need to use @api.depends)
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','contacts'],

    # always loaded
    'data': [
        'views/res_partner_server_action.xml',
        'data/sale_order_scheduled_action.xml',
    ],
    # only loaded in demonstration mode
    'license': 'LGPL-3',
}