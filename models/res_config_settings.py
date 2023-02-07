from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_order = fields.Boolean(string='Sale Order', config_parameter='automated_sale_order.sale_order')
    quotation = fields.Boolean(string='Quotation', config_parameter='automated_sale_order.quotation')
    invoice = fields.Boolean(string='Invoice', config_parameter='automated_sale_order.invoice')
