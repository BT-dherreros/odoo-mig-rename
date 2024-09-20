##############################################################################
# Copyright (c) 2024 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the AGPL-3.0 (http://www.gnu.org/licenses/agpl.html).
# See LICENSE file for full licensing details.
##############################################################################

from odoo import registry
from odoo.addons.account.models.account_move import AccountMove as AccountMoveOrig

import functools
import logging

_logger = logging.getLogger(__name__)

MOD_NAME = 'test_module'


def uninstall_hook(cr, registry):
    # If the methods were patched, we revert them during runtime

    if hasattr(AccountMoveOrig.dummy_operation, 'origin'):
        AccountMoveOrig._revert_method('dummy_operation')


def _if_installed(orig_fn):
    """
    Runs the patched method if installed
    :param orig_fn: Reference to original function to run if not installed.
    :return: decorator for monkey patched method.
    """
    def decorator(new_fn):
        @functools.wraps(new_fn)
        def wrapper(self, *a, **k):
            is_installed = False
            try:
                is_installed = MOD_NAME in registry()._init_modules
            except Exception:
                pass
            if is_installed:
                return new_fn(self, *a, **k)
            return orig_fn(self, *a, **k)
        return wrapper
    return decorator


def post_load():
    @_if_installed(AccountMoveOrig.dummy_operation)
    def dummy_operation(self):
        # TODO: Add here some valid renaming tests.
        return True

    origin = getattr(AccountMoveOrig.dummy_operation, 'origin', None)
    if origin != dummy_operation:
        AccountMoveOrig._patch_method('dummy_operation', dummy_operation)
    _logger.info('AccountMove.dummy_operation method patched to test renaming of models and fieldsZ')
