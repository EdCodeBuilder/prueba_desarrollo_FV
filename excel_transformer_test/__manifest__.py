# -*- coding: utf-8 -*-
{
    'name': "excel_transformer_test",

    'summary': """
        Este es un módulo de testeo para excel_transformer.""",

    'description': """
        Este es un módulo de testeo para excel_transformer.
    """,

    'author': "Eduardo",
    'website': "https://www.eduardo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customs',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
