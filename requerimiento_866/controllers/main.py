# -*- coding: utf-8 -*-
from odoo import http
import random

class ServicesOrder(http.Controller):
    _inherit = 'medical.patient.lab.test'
    
    #Este es el fomato del link
    #/urlsdinamicos?links=https://www.myrconsulting.net,https://www.google.com,https://elcomercio.pe
    @http.route('/urlsdinamicos', type='http', auth='public' , website=True,csrf=False, methods=['GET'] )
    def index(self, **kw):
        links = kw['links']
        enlaces = links.split(',')
        elemento_aleatorio = random.choice(enlaces)
        return http.request.redirect(elemento_aleatorio)