##############################################################################
# Copyright (c) 2024 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the AGPL-3.0 (http://www.gnu.org/licenses/agpl.html).
# See LICENSE file for full licensing details.
##############################################################################

from odoo import api, fields, models

class StockInventoryLineReason(models.Model):
    _inherit = 'stock.inventory.line.reason'

    new_int_field = fields.Integer()
