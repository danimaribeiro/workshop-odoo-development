
import json
from datetime import datetime
from odoo import fields, models
from odoo.exceptions import UserError

from totalvoice.cliente import Cliente


class TotalVoiceSMS(models.Model):
    _name = 'total.voice.sms'

    name = fields.Char()
    number_to = fields.Char()
    message = fields.Char()
    send_date = fields.Datetime()
    state = fields.Selection(
        [('draft', 'Provisório'),
         ('sent', 'Enviado')], default="draft")

    def action_enviar_sms(self):
        cliente = Cliente("571058a184ef75e9b249216e56421c7c",
                          'api.totalvoice.com.br')

        numero_destino = self.number_to
        mensagem = self.message
        response = cliente.sms.enviar(numero_destino, mensagem)

        resposta = json.loads(response)
        if resposta['sucesso']:
            self.send_date = datetime.now()
            self.state = 'sent'
        else:
            raise UserError(resposta['mensagem'])
