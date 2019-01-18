# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 OpenERP SA (<http://www.openerp.com>)
#    Copyright (C) 2011-2015 Serpent Consulting Services Pvt. Ltd. (<http://www.serpentcs.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Web Digital Signature",
    "version": "8.0.0.0.1",
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "category": 'Tools',
    'complexity': "easy",
     'license': 'AGPL-3',
    'depends': ['web'],
    'description': '''
     This module provides the functionality to store digital signature
     for a record.
        -> This  module is helpfull to make your business process a little
           bit more faster & makes it more user friendly by providing you
           digital signature functionality on your documents.
        -> It is touch screen enable so user can add signature with touch
           devices.
        -> Digital signature can be very usefull for documents such as
           sale orders, purchase orders, invoices, payslips, procurement
           receipts, etc.
        The example can be seen into the User's form view where we have
        added a test field under signature.
    ''',
    'summary': '''
     This module provides the functionality to store digital signature
     for a record.
        -> This  module is helpfull to make your business process a little
           bit more faster & makes it more user friendly by providing you
           digital signature functionality on your documents.
        -> It is touch screen enable so user can add signature with touch
           devices.
        -> Digital signature can be very usefull for documents such as
           sale orders, purchase orders, invoices, payslips, procurement
           receipts, etc.
        The example can be seen into the User's form view where we have
        added a test field under signature.
    ''',
    'images': ['static/description/Digital_Signature.jpg'],
    'data': [
        'views/we_digital_sign_view.xml',
        'users_view.xml'
    ],
    'website': 'http://www.serpentcs.com',
    'qweb': ['static/src/xml/digital_sign.xml'],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: