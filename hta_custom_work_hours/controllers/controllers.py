# -*- coding: utf-8 -*-
# from odoo import http


# class HtaCustomWorkHours(http.Controller):
#     @http.route('/hta_custom_work_hours/hta_custom_work_hours/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_custom_work_hours/hta_custom_work_hours/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_custom_work_hours.listing', {
#             'root': '/hta_custom_work_hours/hta_custom_work_hours',
#             'objects': http.request.env['hta_custom_work_hours.hta_custom_work_hours'].search([]),
#         })

#     @http.route('/hta_custom_work_hours/hta_custom_work_hours/objects/<model("hta_custom_work_hours.hta_custom_work_hours"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_custom_work_hours.object', {
#             'object': obj
#         })
