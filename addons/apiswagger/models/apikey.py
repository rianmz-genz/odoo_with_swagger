from odoo import models, fields, api

class ApiKeyModel(models.Model):
    _name = 'apikey.model'

    @api.model
    def getAll(self, params):
        ApiKey = self.env['auth.api.key'].sudo()
        domain = []
        if params.name:
            domain.append(("name", "ilike", params.name))
            
        apikeys = ApiKey.search(domain)
        return [{
            'id': apikey.id,
            'name': apikey.name,
            'key': apikey.key,
            'user': apikey.user_id.name,
        } for apikey in apikeys]