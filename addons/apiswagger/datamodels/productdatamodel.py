from odoo.addons.datamodel.core import Datamodel
from marshmallow import fields

class ProductSearchParam(Datamodel):
    _name = "product.search.param"
    
    id = fields.Integer(required=False, allow_none=False)
    name = fields.String(required=False, allow_none=False)

class ProductCreateRequest(Datamodel):
    _name = "product.create.request"
    
    name = fields.String(required=True, allow_none=False)
    price = fields.Integer(required=True, allow_none=False)
    

class ProductUpdateRequest(Datamodel):
    _name = "product.update.request"
    
    name = fields.String(required=False, allow_none=True)
    price = fields.Integer(required=False, allow_none=True)
