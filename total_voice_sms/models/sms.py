
import json
import re
from datetime import datetime
from odoo import api, fields, models
from odoo.exceptions import UserError

from totalvoice.cliente import Cliente


class TotalVoiceSMS(models.Model):
    _name = 'total.voice.sms'

    name = fields.Char(string="Descrição")
    number_to = fields.Char(string="Enviar para", required=True)
    message = fields.Char(string="Mensagem", required=True)
    send_date = fields.Datetime(string="Data de Envio")
    state = fields.Selection(
        [('draft', 'Provisório'),
         ('sent', 'Enviado')], default="draft", string="Situação")

    @api.onchange('number_to')
    def _onchange_number_to(self):
        numero = re.sub('[^0-9]', '', self.number_to or '')
        if len(numero) == 11:
            self.number_to = '(%s) %s-%s' % (numero[0:2], numero[2:7], numero[7:11])

    def action_enviar_sms(self):
        cliente = Cliente("seu token",
                          'api.totalvoice.com.br')

        numero_destino = re.sub('[^0-9]', '', self.number_to or '')

        mensagem = self.message
        response = cliente.sms.enviar(numero_destino, mensagem)

        resposta = json.loads(response)
        if resposta['sucesso']:
            self.send_date = datetime.now()
            self.state = 'sent'
        else:
            raise UserError(resposta['mensagem'])
