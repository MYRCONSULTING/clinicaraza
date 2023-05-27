import logging
from odoo import fields, models, api
import time
from odoo.exceptions import Warning

logger = logging.getLogger(__name__)

class medicalPatientLabTest(models.Model):
    _inherit = 'medical.patient.lab.test'

    
    @api.onchange('owner_name')
    def onchange_owner_name_2(self):
        for rec in self:
            ###
            records = self.env['account.move'].search([('partner_id','=',rec.owner_name.id)]).ids
            return {'domain': {'invoice_id': [('type', '=', 'out_invoice'), ('state','=','posted'),('id','in',records)]}}
    

    @api.onchange('invoice_id')
    def onchange_invoice_id(self):
        for rec in self:
            rec.date_invoice = rec.invoice_id.invoice_date
    
    invoice_id = fields.Many2one('account.move', string='Facturas')
    date_invoice = fields.Date(string='Fecha de la factura') 
    
    