# -*- coding: utf-8 -*-
{
    'name': "hta_custom_hr",

    'summary': """
        This module add specific HR and Payroll parameter for country Côte d'ivoire (CI).""",

    'description': """
        Long description of module's purpose
    """,

    'author': "HALLTECH AFRICA",
    'website': "http://www.halltech-africa.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',,
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_holidays',
               'hr_payroll',
               ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
