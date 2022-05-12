# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    promotional_discount_check = fields.Boolean()

    # def _compute_promo_discount_check(self):
    #     rec = self.env['ir.config_parameter'].sudo()
    #     self.promotional_discount_check = rec.get_param('practical_exam_2.promotional_discount')

    def action_apply_promotional_discount(self, ):
        promotional_discount = self.env['promotional.discount'].search([])
        order_product_ids = self.order_line.product_id
        product_ids_list = [product.id for product in order_product_ids]
        discount_id = self.env.ref("practical_exam_2.product_category_offers").id
        for offer in product_ids_list:
            if discount_id == offer:
                raise ValidationError(_('Sorry, You can add one discount coupon...'))

        discount_rec = promotional_discount.filtered(lambda record: record.start_date <= self.date_order <= record.end_date
                                                     and self.amount_untaxed >= record.minimum_order_amount)
        discount_rec_error = [res.id for res in discount_rec]
        if len(discount_rec_error) == 0:
            raise ValidationError(_('Sorry, You are not applicable for any discount coupon...'))

        discount_percentage = [(self.amount_untaxed * i.discount) / 100 for i in discount_rec if
                               i.discount_type == 'percentage']
        per_name_list = [p_dis_price for p_dis_price in discount_rec if p_dis_price.discount_type == 'percentage']

        fix_price = [dis_price for dis_price in discount_rec if dis_price.discount_type == 'fixed_amount']
        for rec in discount_rec:
            if rec.discount_type == 'percentage' or rec.discount_type == 'fixed_amount':
                if len(fix_price) == 0:
                    min_p = min([res.discount for res in per_name_list])
                    per_name = (self.env['promotional.discount'].search(
                        [('discount', '=', min_p), ('discount_type', '=', 'percentage')]))
                    min_percentage = min(discount_percentage)
                    min_per = -(min_percentage)
                    self.write({'order_line': [(0, 0, {'product_id': discount_id,
                                                       'name': per_name.name,
                                                       'price_unit': min_per})]})
                    break
                elif len(per_name_list) == 0:
                    min_fix_dic = min([res.discount for res in fix_price])
                    fix_dic_name = (self.env['promotional.discount'].search(
                        [('discount', '=', min_fix_dic), ('discount_type', '=', 'fixed_amount')]))
                    discount = -(min_fix_dic)
                    self.write({'order_line': [(0, 0, {'product_id': discount_id,
                                                       'name': fix_dic_name.name,
                                                       'price_unit': discount})]})
                    break
                else:
                    min_p = min([res.discount for res in per_name_list])
                    per_name = (self.env['promotional.discount'].search(
                        [('discount', '=', min_p), ('discount_type', '=', 'percentage')]))
                    min_percentage = min(discount_percentage)
                    min_per = -(min_percentage)
                    min_fix_dic = min([res.discount for res in fix_price])
                    fix_dic_name = (self.env['promotional.discount'].search(
                        [('discount', '=', min_fix_dic), ('discount_type', '=', 'fixed_amount')]))
                    if min_fix_dic > min_percentage:
                        self.write({'order_line': [(0, 0, {'product_id': discount_id,
                                                           'name': per_name.name,
                                                           'price_unit': min_per})]})
                        break
                    else:
                        discount = -(min_fix_dic)
                        self.write({'order_line': [(0, 0, {'product_id': discount_id,
                                                           'name': fix_dic_name.name,
                                                           'price_unit': discount})]})
                        break
