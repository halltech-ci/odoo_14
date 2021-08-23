# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProductCategory(models.Model):
    _inherit = "product.category"

    code = fields.Char(
        default="/",
        index=True,
    )

    @api.returns("self", lambda value: value.id)
    def copy(self, default=None):
        default = default or {}
        default.setdefault("code", self.code + _("-copy"))
        return super().copy(default)