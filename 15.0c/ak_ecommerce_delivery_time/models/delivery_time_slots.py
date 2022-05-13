# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DeliveryTimeSlots(models.Model):
    _name = "delivery.time.slots"
    _description = "Mange Delivery Time Slots"
    _rec_name = 'slot_name'

    slot_name = fields.Selection([('morning', 'Morning'), ('afternoon', 'Afternoon'),
                                  ('evening', 'Evening'), ('night', 'Night')])
    time_slot = fields.Selection([('fir_time_slot', '9AM-12PM'),
                                  ('sec_time_slot', '12PM-4PM'),
                                  ('third_time_slot', '4PM-7PM'),
                                  ('four_time_slot', '7PM-10PM')])
    state = fields.Selection([('active', 'Active'), ('cancel', 'Cancel')])
    comments = fields.Html()

    @api.onchange('time_slot')
    def _onchange_for_slot_name(self):
        if self.time_slot == 'fir_time_slot':
            self.slot_name = 'morning'
        if self.time_slot == 'sec_time_slot':
            self.slot_name = 'afternoon'
        if self.time_slot == 'third_time_slot':
            self.slot_name = 'evening'
        if self.time_slot == 'four_time_slot':
            self.slot_name = 'night'


