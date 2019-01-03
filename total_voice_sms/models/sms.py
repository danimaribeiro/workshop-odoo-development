

from odoo import fields, models


class TotalVoiceSMS(models.Model):
    _name = 'total.voice.sms'

    name = fields.Char()
    number_to = fields.Char()
    message = fields.Char()
