# -*- coding: utf-8 -*-

from odoo import models, fields


class iut_classe(models.Model):
    _name = 'iut.classe'
    name = fields.Char(string='nom classe')
    level = fields.Selection([('seconde', 'Seconde'), ('premiere', 'Premiere'), ('terminale', 'Terminale')], string='Niveau')
    agenda_id = fields.One2many('iut.agenda', 'classe_id', string='Agenda')
    student_nb = fields.Char(string='nombre d\'éleves')
    professeur_id = fields.Many2one('iut.professeur', string='professeur')
    eleve_id = fields.One2many('iut.eleve','classe_id', string='eleve')