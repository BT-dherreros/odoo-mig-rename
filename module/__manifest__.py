##############################################################################
# Copyright (c) 2024 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the AGPL-3.0 (http://www.gnu.org/licenses/agpl.html).
# See LICENSE file for full licensing details.
##############################################################################
{
    'name': 'Test Module for The Migration Renaming Script',
    'author': 'braintec AG',
    'license': 'AGPL-3',
    'version': '13.0.1.0.1',
    'summary': 'This modules is designed to be tested between a it\'s manifest version and a target version',
    'category': 'Tools/Migration',
    'website': 'https://braintec.com',
    'depends': [
    ],
    'data': [
        'data/test_data.xml',

        'security/test_rules.xml',

        'views/account_move.xml',
    ],
    'installable': False,
    'application': False,
    'auto_install': False,
    'post_load': 'post_load',
    'uninstall_hook': 'uninstall_hook',
}
