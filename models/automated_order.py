from odoo import models


class AutomatedOrder(models.Model):
    _inherit = "product.product"

    def button_so(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'wizard',
            'view_mode': 'form',
            'res_model': 'sale.order.wizard',
            'target': 'new',
            'context': {'default_price': self.list_price,
                        'default_product_id': self.id}
        }

    def get_sale_order(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Order',
            'view_mode': 'tree,form',
            'res_model': 'sale.order',
            'context': [('create', '=', False)]
    }




