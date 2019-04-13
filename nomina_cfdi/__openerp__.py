# -*- coding: utf-8 -*-

{
    'name': 'Nomina Electrónica para México CFDI v1.2',
    'summary': 'Agrega funcionalidades para timbrar la nómina electrónica en México.',
    'description': '''
    Nomina CFDI Module
    ''',
    'author': 'IT Admin',
    'version': '1.0',
    'category': 'Employees',
    'depends': [
        'base', 'hr', 'hr_payroll', 'catalogos_cfdi'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/hr_employee_view.xml',
        'views/hr_contract_view.xml',
        'views/hr_salary_view.xml',
        'views/hr_payroll_payslip_view.xml',
        'views/tablas_cfdi_view.xml',
        'views/res_company_view.xml',
        'report/report_payslip.xml',
        'data/mail_template_data.xml',
    ],
    'installable': True,
    'application': False
}