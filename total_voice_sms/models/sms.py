
from odoo import fields, models
from odoo.exceptions import UserError


class TotalVoiceSMS(models.Model):
    _name = 'total.voice.sms'

    name = fields.Char()
    number_to = fields.Char()
    message = fields.Char()
    send_date = fields.Datetime()

    def action_enviar_sms(self):
        raise UserError('Já vou implementar')
