import logging
from odoo import fields, models, api
import time
from odoo.exceptions import Warning

logger = logging.getLogger(__name__) 

class resPartner(models.Model):
    _inherit = "res.partner"
    x_patient_count = fields.Integer(string="Pacientes")
    patient_ids = fields.One2many('medical.patient',compute='_get_patients', string='Pacientes', copy=False)

    
    #@api.multi
    def _get_patients(self):
        for doc in self:
            listapacientes = self.env['medical.patient'].search([('current_address', '=', doc.id)]).ids
            doc.patient_ids= [(6, 0,listapacientes)]
            doc.x_patient_count = len(listapacientes) or 0
    '''
    '''
    #@api.multi
    def action_view_pacientes(self):
        return {
            'name': 'Pacientes',
            'view_type': 'form',
            'view_mode': 'tree,form,pivot',
            'res_model': 'medical.patient',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', self.mapped('patient_ids.id'))],
        }
    
    
    
