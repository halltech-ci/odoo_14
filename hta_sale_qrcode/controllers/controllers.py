# -*- coding: utf-8 -*-
# from odoo import http


# class HtaSaleQrcode(http.Controller):
#     @http.route('/hta_sale_qrcode/hta_sale_qrcode/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_sale_qrcode/hta_sale_qrcode/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_sale_qrcode.listing', {
#             'root': '/hta_sale_qrcode/hta_sale_qrcode',
#             'objects': http.request.env['hta_sale_qrcode.hta_sale_qrcode'].search([]),
#         })

#     @http.route('/hta_sale_qrcode/hta_sale_qrcode/objects/<model("hta_sale_qrcode.hta_sale_qrcode"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_sale_qrcode.object', {
#             'object': obj
#         })
