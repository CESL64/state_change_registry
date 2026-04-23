import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class StateChangeRegistry(models.Model):
    _name = "state.change.registry"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "State Change Registry"
    _order = "change_date desc, id desc"

    name = fields.Char(string="Nombre", required=True)
    document_type = fields.Selection(
        selection=[
            ("invoice", "Factura"),
            ("sale", "Documento de venta"),
            ("purchase", "Documento de compra"),
        ],
        string="Tipo de documento",
        required=True,
    )
    change_date = fields.Datetime(
        string="Fecha",
        required=True,
        default=fields.Datetime.now,
    )
    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Usuario",
        required=True,
        default=lambda self: self.env.user,
        readonly=True,
    )
    amount = fields.Monetary(string="Monto", currency_field="currency_id")
    line_count = fields.Integer(string="Cantidad de lineas")
    tax_summary = fields.Text(string="Impuestos")
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Compania",
        required=True,
        default=lambda self: self.env.company,
    )
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        string="Moneda",
        related="company_id.currency_id",
        store=True,
        readonly=True,
    )
    previous_state = fields.Char(string="Estado previo")
    new_state = fields.Char(string="Estado nuevo")
    mail_sent = fields.Boolean(string="Correo enviado", default=False)

    def send_state_change_notification(self):
        """Hook base para que modulos dependientes implementen envio de correo."""
        return

    @api.model
    def cron_send_pending_state_change_notifications(self):
        pending_records = self.search([("mail_sent", "=", False)])
        for record in pending_records:
            try:
                record.send_state_change_notification()
            except Exception:
                _logger.exception(
                    "Error enviando notificacion de cambio de estado para registro ID %s",
                    record.id,
                )
