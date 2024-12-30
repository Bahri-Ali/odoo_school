{
    'name': ' School dz ',
    'version': '1.0',
    'summary': 'Module for managing school operations efficiently',
    'description': """
        All about managing students, teachers, and school operations.
    """,
    'author': 'Ali Bahri',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/nav.xml',
        'views/student.xml',
        'views/tetcher.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}