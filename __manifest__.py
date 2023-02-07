{
    'name': 'Automated Sale Order',
    'version': "16.0.1.0.0",
    'sequence': -1,
    'installable': True,
    'application': True,
    'depends': ['product', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_wizard.xml',
        'views/automated_order.xml',
        'views/res_config_settings_views.xml',
    ]
}