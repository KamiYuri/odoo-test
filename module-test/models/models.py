# -*- coding: utf-8 -*-

from odoo import models, fields


class Customer(models.Model):
    _name = 'customer'
    _description = 'Customer'

    name = fields.Char(string='Name', required=True)
    avatar = fields.Binary(string='Avatar', attachment=True)
    country = fields.Char(string='Country')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    day_of_birth = fields.Datetime(string='Day of birth')
    tags = fields.Selection([('normal', 'Normal'), ('vip', 'Vip')], default='normal', string='Tag', required=True)
