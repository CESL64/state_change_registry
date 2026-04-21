from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    not_registry_change = fields.Boolean(string="Sin registro de estado")
