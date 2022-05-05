""" This model is create for student page """
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ContactSale(models.Model):
    """ This class is for student model this model is for student page"""
    _name = 'contact.sale'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'contact sale'

    name = fields.Char(string='(Ir Sequence)', required=True, copy=False,
                       readonly=True, default=lambda self: _('New'))
    partner_id = fields.Many2one(comodel_name='res.partner', string='Contact', required=True, tracking=True)
    sale_order_id = fields.Many2one(comodel_name='sale.order', string="Sale Order", tracking=True)
    salesperson_id = fields.Many2one(comodel_name='res.users', related='sale_order_id.user_id', tracking=True)
    no_of_follow_upw = fields.Integer(string='Follow UPS', readonly=True)
    contact_sale_history_lines_ids = fields.One2many('contact.sale.history', 'partner_sale_id')
    state = fields.Selection([('draft', 'Draft'), ('sent', 'In Progress'),
                              ('sale', 'Done'),
                              ('cancel', 'Cancel')],
                             string='status', tracking=True)

    ''' This function change the state of form by clicking on confirm button '''
    def action_sent(self):
        state_values = (dict(self._fields['state'].selection).get(self.state))
        old_status = state_values
        old_follow = self.no_of_follow_upw
        self.write({'state': 'sent'})
        self.no_of_follow_upw += 1
        state_values = (dict(self._fields['state'].selection).get(self.state))
        new_status = state_values
        new_follow = self.no_of_follow_upw
        values = {
            'old_n_of_follow_ups': old_follow,
            'new_n_of_follow_ups': new_follow,
            'old_state': old_status,
            'new_state': new_status,
        }
        self.write({
            'contact_sale_history_lines_ids': [(0, 0, values)]
        })

    def action_draft(self):
        state_values = (dict(self._fields['state'].selection).get(self.state))
        old_follow = self.no_of_follow_upw
        old_status = state_values
        self.write({'state': 'draft'})
        self.no_of_follow_upw += 1
        state_values = (dict(self._fields['state'].selection).get(self.state))
        new_status = state_values
        new_follow = self.no_of_follow_upw
        values = {
            'old_n_of_follow_ups': old_follow,
            'new_n_of_follow_ups': new_follow,
            'old_state': old_status,
            'new_state': new_status,
        }
        self.write({
            'contact_sale_history_lines_ids': [(0, 0, values)]
        })

    def action_sale(self):
        state_values = (dict(self._fields['state'].selection).get(self.state))
        old_follow = self.no_of_follow_upw
        old_status = state_values
        self.write({'state': 'sale'})
        self.no_of_follow_upw += 1
        state_values = (dict(self._fields['state'].selection).get(self.state))
        new_status = state_values
        new_follow = self.no_of_follow_upw
        values = {
            'old_n_of_follow_ups': old_follow,
            'new_n_of_follow_ups': new_follow,
            'old_state': old_status,
            'new_state': new_status,
        }
        self.write({
            'contact_sale_history_lines_ids': [(0, 0, values)]
        })
        template_id = self.env.ref('practical_exam.email_template_contact_sale').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

    def action_cancel(self):
        state_values = (dict(self._fields['state'].selection).get(self.state))
        old_follow = self.no_of_follow_upw
        old_status = state_values
        self.write({'state': 'cancel'})
        self.no_of_follow_upw += 1
        state_values = (dict(self._fields['state'].selection).get(self.state))
        new_status = state_values
        new_follow = self.no_of_follow_upw
        values = {
            'old_n_of_follow_ups': old_follow,
            'new_n_of_follow_ups': new_follow,
            'old_state': old_status,
            'new_state': new_status,
        }
        self.write({
            'contact_sale_history_lines_ids': [(0, 0, values)]
        })

    @api.model
    def create(self, values):
        """ for generate a sequence of contact sale"""
        if values.get('name', _('New')) == _('New'):
            values['name'] = self.env['ir.sequence'].next_by_code('contact.sale') or _('New')
        res = super(ContactSale, self).create(values)
        return res

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    contact_sale_count = fields.Integer(compute='_compute_contact_sale_count', invisible='1')

    def _compute_contact_sale_count(self):
        contact_sale_count = self.env['contact.sale'].search_count([('partner_id', '=', self.ids)])
        self.contact_sale_count = contact_sale_count

    def action_open_available_contact_sale(self):
        if self.contact_sale_count == 1:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Contact Sale',
                'res_model': 'contact.sale',
                'view_mode': 'form',
                'view_type': 'form',
                'view_id': self.env.ref("practical_exam.contact_sale_view_form").id,
                'domain': [('partner_id', '=', self.ids)],
                'target': 'self',
            }
        if self.contact_sale_count > 1:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Contact Sale',
                'res_model': 'contact.sale',
                'domain': [('partner_id', '=', self.ids)],
                'view_mode': 'tree,form',
                'target': 'current',
            }
        if self.contact_sale_count < 1:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Contact Sale',
                'res_model': 'contact.sale',
                'domain': [('partner_id', '=', self.ids)],
                'view_mode': 'form',
                'target': 'current',
            }