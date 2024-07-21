# -*- coding: utf-8 -*-
{
    'name': "apiswagger",

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
    'depends': ['base', 'base_rest_datamodel', 'base_rest_auth_api_key', 'sale_management', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/sales_dashboard.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
   'qweb': [
        'static/src/components/sakes_dashboard.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'my_owl_module/static/src/components/sakes_dashboard.js',
            'my_owl_module/static/src/components/sakes_dashboard_init.js',
        ],
    },

}
