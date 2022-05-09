# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import fields, models, api,_

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    promotional_discount_check = fields.Boolean(compute="_compute_promo_discount_check")


    def _compute_promo_discount_check(self):
        rec = self.env['ir.config_parameter'].sudo()
        self.promotional_discount_check = rec.get_param('practical_exam_2.promotional_discount')


    def action_apply_promotional_discount(self,):

        promotional_discount = self.env['promotional.discount'].search([])
        a=self.id
        b=self.browse([a])
        print('\n\n',b)
        print('\n\norder',b.name,'\n\n',b.order_line)

        active_id = self.env['sale.order']._context.get('active_id')
        print('\n\n',active_id)
        # read_list = self.env['sale.order']
        read_list=b.search([])

        list1 = (read_list.read(['order_line']))
        for rec in list1:
            print(rec)

        print('\n\npromotional_discount', promotional_discount)
        discount_id = self.env.ref("practical_exam_2.product_category_offers").id
        # if self.env['sale.order'].search([discount_id, 'in', 'order_line']):
        #     print('\n\n\nHello', 'Yellow')
        print('\n\ndiscount_id', discount_id, '\n\nres',)

        discount_rec = promotional_discount.filtered(lambda record:
                                                     self.date_order >= record.start_date
                                                     and self.date_order <= record.end_date
                                                     and self.amount_untaxed >= record.minimum_order_amount)
        print('\n\nello',discount_rec)
        print('\n\namount_untaxed', self.amount_untaxed)
        fix_price = [dis_price for dis_price in discount_rec if dis_price.discount_type == 'fixed_amount']
        for fix_price_rec in discount_rec:
            if fix_price_rec.discount_type == 'fixed_amount':
                min_of_fix_dic = min(fix_price)
        print('\n\n\nb', min_of_fix_dic)

        discount_percentage = [(self.amount_untaxed*i.discount)/100 for i in discount_rec if i.discount_type == 'percentage']
        for rec in discount_rec:
            if rec.discount_type == 'percentage':
                min_percentage = min(discount_percentage)
                if min_of_fix_dic.discount > min_percentage:
                    self.write({'order_line': [(0, 0, {'product_id': discount_id,
                                               'price_subtotal': min_percentage})]})
                    print('heyy')
                    break
                else:
                    discount = -(min_of_fix_dic.discount)
                    print("\n\n", type(discount), discount)
                    self.write({'order_line': [(0, 0, {'product_id': discount_id,
                                                       'price_unit': discount})]})
                    print('How')
                    break
        print('\n\n\nd', min_percentage, '\n\n')

























        # d = [(self.amount_untaxed-i.discount) for i in b if i.discount_type == 'fixed_amount']
        # print('\n\n\n',d,'\n\n')
        # if min(c) > min(d)
        # min_discount=min(min(discount_percentage),min([i.discount for i in discount_rec if i.discount_type == 'fixed_amount']))
        # print('a',min_discount)
        # for dis_product in discount_rec:
        #     if dis_product.discount_type == 'fixed_amount':
        #         if dis_product.discount < discount_percentage:
        #             print('\n\nHeyyyy')
        #             # self.env['product.product'].create({'name': dis_product.name})
        #     elif dis_product.discount_type == 'percentage':
        #         p_p=[(self.amount_untaxed * i.discount) / 100 for i in discount_rec if i.discount_type == 'percentage']
        #         a=min('p-p')
        #         if a < dis_product.discount:
        #             print('\n\n\nPP',p_p)
        #             # self.env['product.product'].create({'name': dis_product.name})


        # print(self.id)
        # for s in discount_rec:
        #     self.write({'order_line': [(0, 0, {'product_id': s.id,
        #                                        'price_unit': s.discount, 'price_subtotal': min_discount})]})
