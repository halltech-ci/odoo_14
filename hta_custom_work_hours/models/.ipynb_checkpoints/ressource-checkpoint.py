# -*- coding: utf-8 -*-

from odoo import models, fields, api

"""
class RessourceCalendar(models.Model):
    _inherit = "ressource.calendar"
"""
    


class RessourceCalendarAttendance(models.Model):
    _inherit = "ressource.calendar.attendance"
    
    day_period = fields.Selection(selection_add=[('night', 'Night')])
    day_range = fields.Selection([('first', 'First'), ('second', 'Second'), ('third', 'Third')], required=True, default='first')