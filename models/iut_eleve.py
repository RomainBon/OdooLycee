# -*- coding: utf-8 -*-

from odoo import models, fields


class iut_eleve(models.Model):
    _name = 'iut.eleve'
    name = fields.Char(string='nom')
    surname = fields.Char(string='prénom')
    birthdate = fields.Date(string='date de naissance')
    age = fields.Integer(string='age')
    classe_id = fields.Many2one('iut.classe', string='classe')