{
    'name': 'Mail Template Data',
    'version': '15.0.1.0',
    'category': 'Tools',
    'summary': 'Import template for email',
    'description': """
        This module import specific data for JumpTo client
    """,
    'author': 'JumpTo',
    'website': 'https://jumpto.ch',
    'depends': ['mail', 'sale','account'],
    'data': [
        'data/accompte_salutation_template.xml',
        'data/facture_salutation_template.xml',
        'data/devis_salutaion_template.xml',
    ],
    'installable': True,
    'auto_install': False,
}
