from odoo.addons.datamodel.core import Datamodel
from marshmallow import fields

class ApiKeySearchParam(Datamodel):
    _name = "apikey.search.param"
    
    name = fields.String(required=False, allow_none=False)