# -*- coding: utf-8 -*-

from odoo import models, fields


class ModuleAModel(models.Model):
    _name = 'module_a.module_a_model'
    _description = 'This is my model'

    name = fields.Char(string='Name', required=True)
    value = fields.Integer(string='Value', required=True)
    description = fields.Text(string='Description')
    image_url = fields.Char(string='Image URL')

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
