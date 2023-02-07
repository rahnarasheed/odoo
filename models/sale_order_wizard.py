from odoo import models, fields


class SaleOrderWizard(models.TransientModel):
    _name = 'sale.order.wizard'

    product_id = fields.Many2one("product.product", Strings="product")
    customer_id = fields.Many2one("res.partner", string="Customer")
    quantity = fields.Integer(string="Quantity", default=1)
    price = fields.Float(string="Price")

    # sale_id = fields.Many2one("sale.order")

    def button_confirm(self):
        # rec = self.env['sale.order']
        sale_order = self.env['ir.config_parameter'].sudo().get_param('automated_sale_order.sale_order')
        quotation = self.env['ir.config_parameter'].sudo().get_param('automated_sale_order.quotation')
        invoice = self.env['ir.config_parameter'].sudo().get_param('automated_sale_order.invoice')
        print(sale_order)
        if sale_order:
            order = self.env['sale.order'].search(
                [('partner_id.id', '=', self.customer_id.id), ('state', '=', 'draft')])
            print(order, "1234")
            if order:
                for line in order:
                    print(line, "ll")
                    record = line.update({
                        'order_line': [(0, 0, {
                            'name': self.product_id.name,
                            'product_template_id': self.product_id.id,
                            'product_id': self.product_id.id,
                            'product_uom_qty': self.quantity,
                            'price_unit': self.price,
                        })]
                    })
                    line.action_confirm()
            else:
                order = self.env['sale.order'].create({
                    'partner_id': self.customer_id.id,
                    # 'state': 'sale',
                    'order_line': [(0, 0, {
                        'name': self.product_id.name,
                        'product_template_id': self.product_id.id,
                        'product_id': self.product_id.id,
                        'product_uom_qty': self.quantity,
                        'price_unit': self.price,
                    })]
                })
            order.action_confirm()
        elif quotation:
            order = self.env['sale.order'].search(
                [('partner_id.id', '=', self.customer_id.id), ('state', '=', 'draft')])
            print(order, "1234")
            if order:
                for line in order:
                    print(line, "ll")
                    record = line.update({
                        'order_line': [(0, 0, {
                            'name': self.product_id.name,
                            'product_template_id': self.product_id.id,
                            'product_id': self.product_id.id,
                            'product_uom_qty': self.quantity,
                            'price_unit': self.price,
                        })]
                    })
            else:
                order = self.env['sale.order'].create({
                    'partner_id': self.customer_id.id,
                    # 'state': 'sale',
                    'order_line': [(0, 0, {
                        'name': self.product_id.name,
                        'product_template_id': self.product_id.id,
                        'product_id': self.product_id.id,
                        'product_uom_qty': self.quantity,
                        'price_unit': self.price,
                    })]
                })
        elif invoice:
            order = self.env['sale.order'].search(
                [('partner_id.id', '=', self.customer_id.id), ('state', '=', 'draft')])
            print(order, "1234")
            if order:
                for line in order:
                    print(line, "ll")
                    record = line.update({
                        'order_line': [(0, 0, {
                            'name': self.product_id.name,
                            'product_template_id': self.product_id.id,
                            'product_id': self.product_id.id,
                            'product_uom_qty': self.quantity,
                            'price_unit': self.price,
                        })]
                    })
                    line.action_confirm()
                    line._create_invoices()
            else:
                order = self.env['sale.order'].create({
                    'partner_id': self.customer_id.id,
                    # 'state': 'sale',
                    'order_line': [(0, 0, {
                        'name': self.product_id.name,
                        'product_template_id': self.product_id.id,
                        'product_id': self.product_id.id,
                        'product_uom_qty': self.quantity,
                        'price_unit': self.price,
                    })]
                })
                order.action_confirm()
                order._create_invoices()






    #
    # else:
    #     sale = rec.create({
    #         'partner_id': self.customer_id.id,
    #         # 'state': 'sale',
    #         'order_line': [(0, 0, {
    #             'name': "sddd",
    #             'product_template_id': self.product_id.id,
    #             'product_id': self.product_id.id,
    #             'product_uom_qty': self.quantity,
    #             'price_unit': self.price,
    #         })]
    #     })
    #     sale.action_confirm()

    # self.env['sale.order'].action_confirm()
    # self.env['sale.order'].state = 'sale'
    # self.sale_id.state ="sale"
    # print(self, "hey")
    # # active_id = self.env.context.get('active_id')
    # # order = self.browse(active_id)
    # # print(order.id,"erty")
    # # # print(order.name,"erty")
    # # self.product_id = order.id
    # abc = self.env['sale.order'].create({
    #     'partner_id': self.customer_id.id,
    #     # 'state': 'sale',
    #     'order_line': [(0, 0, {
    #         'name': "sddd",
    #         'product_template_id': self.product_id.id,
    #         'product_id': self.product_id.id,
    #         'product_uom_qty': self.quantity,
    #         'price_unit': self.price,
    #     })]
    # })
    # abc.action_confirm()
    # abc = self.env['sale.order']
    # abc.write({'state': 'sale'})

    # def button_confirm(self):
    #     print("hey")
    # #     rec = self.env['sale.order']
    #     self.env['sale.order'].create({
    #         'partner_id': self.customer_id,
    #         # 'order_line': [(0, 0, {
    #         #             "quantity": rec.qty_to_invoice
    #         #         })]
    #     })
    #     self.env['sale.order'].action_confirm()
    #     print('rahanaaaaaaaaaaaaaaaaaaaaaaaaaa')
