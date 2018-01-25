# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class translate(models.Model):
    _name = 'translate.translate'

    name = fields.Char(_(u'Name'))
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    value3 = fields.Float(compute="_value_pc")
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100
        self.value3 = float(self.value) / 100
