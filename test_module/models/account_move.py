##############################################################################
# Copyright (c) 2024 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the AGPL-3.0 (http://www.gnu.org/licenses/agpl.html).
# See LICENSE file for full licensing details.
##############################################################################

from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    new_char_field = fields.Char()
    new_m2o_field_renamed_id = fields.Many2one('stock.inventory.line.reason')

    @api.model
    def dummy_method_with_models_and_fields_to_rename(self):
        '''
            This dummy method models and fields are supposed to be renamed by mig_rename.py
        '''
        for move in self:
            if move.type == 'out_invoice':
                move.new_m2o_field_renamed_id = self.env['stock.inventory.line.reason'].search([
                    'field_renamed', '=', 'TEST'
                ])
