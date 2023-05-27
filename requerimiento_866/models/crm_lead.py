import logging
from odoo import fields, models, api
import time
from odoo.exceptions import Warning
import random

logger = logging.getLogger(__name__)

class crmLead(models.Model):
    _inherit = 'crm.lead'
    
    @api.model
    def create(self, vals):
        '''Create contact in hubspot on create of partner in Odoo.'''
        listavendedores = self.env['crm.team'].browse(int(vals['team_id'])).team_user_ids
        
        elemento_aleatorio = random.choice(listavendedores)
        #raise Warning(str(elemento_aleatorio))
        if int(elemento_aleatorio):
            user_id = self.env['team.user'].browse(int(elemento_aleatorio)).user_id
            vals['user_id'] = int(user_id)
        return super(crmLead, self).create(vals)
        

    
    
    
    