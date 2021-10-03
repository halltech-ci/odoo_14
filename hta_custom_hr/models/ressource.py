# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RessourceCalendar(models.Model):
    _inherit = "ressource.calendar"
    
    @api.model
    def default_get(self, fields):
        res = super(ResourceCalendar, self).default_get(fields)
        if not res.get('name') and res.get('company_id'):
            res['name'] = _('Working Hours of %s', self.env['res.company'].browse(res['company_id']).name)
        if 'attendance_ids' in fields and not res.get('attendance_ids'):
            company_id = res.get('company_id', self.env.company.id)
            company = self.env['res.company'].browse(company_id)
            company_attendance_ids = company.resource_calendar_id.attendance_ids
            if company_attendance_ids:
                res['attendance_ids'] = [
                    (0, 0, {
                        'name': attendance.name,
                        'dayofweek': attendance.dayofweek,
                        'hour_from': attendance.hour_from,
                        'hour_to': attendance.hour_to,
                        'day_period': attendance.day_period,
                    })
                    for attendance in company_attendance_ids
                ]
            else:
                res['attendance_ids'] = [
                    (0, 0, {'name': _('Monday Morning'), 'dayofweek': '0', 'hour_from': 8, 'hour_to': 12, 'day_period': 'morning'}),
                    (0, 0, {'name': _('Monday Afternoon'), 'dayofweek': '0', 'hour_from': 13, 'hour_to': 17, 'day_period': 'afternoon'}),
                    (0, 0, {'name': _('Tuesday Morning'), 'dayofweek': '1', 'hour_from': 8, 'hour_to': 12, 'day_period': 'morning'}),
                    (0, 0, {'name': _('Tuesday Afternoon'), 'dayofweek': '1', 'hour_from': 13, 'hour_to': 17, 'day_period': 'afternoon'}),
                    (0, 0, {'name': _('Wednesday Morning'), 'dayofweek': '2', 'hour_from': 8, 'hour_to': 12, 'day_period': 'morning'}),
                    (0, 0, {'name': _('Wednesday Afternoon'), 'dayofweek': '2', 'hour_from': 13, 'hour_to': 17, 'day_period': 'afternoon'}),
                    (0, 0, {'name': _('Thursday Morning'), 'dayofweek': '3', 'hour_from': 8, 'hour_to': 12, 'day_period': 'morning'}),
                    (0, 0, {'name': _('Thursday Afternoon'), 'dayofweek': '3', 'hour_from': 13, 'hour_to': 17, 'day_period': 'afternoon'}),
                    (0, 0, {'name': _('Friday Morning'), 'dayofweek': '4', 'hour_from': 8, 'hour_to': 12, 'day_period': 'morning'}),
                    (0, 0, {'name': _('Friday Afternoon'), 'dayofweek': '4', 'hour_from': 13, 'hour_to': 17, 'day_period': 'afternoon'})
                ]
        return res