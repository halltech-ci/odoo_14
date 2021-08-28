# -*- coding: utf-8 -*-

from odoo import models, fields, api
import qrcode
from io import BytesIO
import base64

class ProductQrcode(models.Model):
    _inherit = "product.template"
    _description = "Product template QR code"

    qr_code = fields.Binary("QR Code", attachment=True, store=True)

    @api.onchange('default_code')
    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=3,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.default_code)
        qr.make(fit=True)
        img = qr.make_image(fill_color="blue", back_color="white")
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_image = base64.b64encode(temp.getvalue())
        self.qr_code = qr_image
        
        
class ProductQrcode(models.Model):
    _inherit = "product.template"
    _description = "Product template QR code"

    qr_code = fields.Binary("QR Code", attachment=True, store=True)

    @api.onchange('default_code')
    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=3,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.default_code)
        qr.make(fit=True)
        img = qr.make_image(fill_color="blue", back_color="white")
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_image = base64.b64encode(temp.getvalue())
        self.qr_code = qr_image