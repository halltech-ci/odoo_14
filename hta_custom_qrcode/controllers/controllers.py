# -*- coding: utf-8 -*-
# from odoo import http


# class HtaCustomQrcode(http.Controller):
#     @http.route('/hta_custom_qrcode/hta_custom_qrcode/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_custom_qrcode/hta_custom_qrcode/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_custom_qrcode.listing', {
#             'root': '/hta_custom_qrcode/hta_custom_qrcode',
#             'objects': http.request.env['hta_custom_qrcode.hta_custom_qrcode'].search([]),
#         })

#     @http.route('/hta_custom_qrcode/hta_custom_qrcode/objects/<model("hta_custom_qrcode.hta_custom_qrcode"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_custom_qrcode.object', {
#             'object': obj
#         })
