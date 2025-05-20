# -*- coding: utf-8 -*-
{
    'name': 'PT Laudza Project Reporting',
    'version': '1.0',
    'summary': 'Digital Project Reporting System',
    'description': """
        Digital Project Reporting System for PT Laudza Engineer Consultant.
        This module allows project managers and technical staff to:
        - Create and manage project reports
        - Upload visual documentation
        - Track project progress
        - Record and manage project constraints
        - Provide feedback and guidance
    """,
    'category': 'Project',
    'author': 'Kelompok 10',
    'website': '',
    'depends': ['base', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/action.xml',
        'views/project.xml',
        'views/project_item.xml',
        'views/project_kendala.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': -100,
}