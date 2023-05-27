import logging
from odoo import fields, models, api
import time
from odoo.exceptions import Warning

logger = logging.getLogger(__name__)

class medicalPatient(models.Model):
    _name = "medical.patient"
    _inherit = ['medical.patient','mail.thread']

    #contacto_id = fields.Many2one('res.partner', string='Contacto')
     