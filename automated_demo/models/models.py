# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class automated_demo(models.Model):
    _name = 'automated.demo'

    name = fields.Char()
    expire_date = fields.Date()
    alert = fields.Boolean()

    @api.model
    def automate(self, *args, **kwargs):
        print (args)
        print ("on automate", args[0])
        condition_date = args[0]
        condition_date = datetime.strptime(args[0], "%Y-%m-%d")
        print (condition_date, type(condition_date))
        for rec in self.search([]):
            date = datetime.strptime(rec.expire_date, "%Y-%m-%d")
            if date > condition_date:
                print (date, ' > ', condition_date)
            else:
                print (date, ' < ', condition_date)
            # date = datetime.strptime('%Y-%m-%d')
            # print (rec.expire_date, type(rec.expire_date))
        return True
