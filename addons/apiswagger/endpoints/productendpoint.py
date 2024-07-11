from marshmallow import fields, Schema

from odoo.addons.base_rest import restapi
from odoo.addons.component.core import Component
from odoo.addons.datamodel.core import Datamodel

class ProductNewApiService(Component):
    _inherit = "base.rest.service"
    _name = "product.new_api.service"
    _usage = "product"
    _collection = "base.private"
    _description = """
        Product New API Services
        Services developed with the new api provided by base_rest
    """
    _default_auth = "api_key"

    _input_get_all = restapi.Datamodel("product.search.param")
    _input_create = restapi.Datamodel("product.create.request")
    _input_update = restapi.Datamodel("product.update.request")
    _input_delete = restapi.Datamodel("product.delete.request")
    _input_get_by_id = restapi.Datamodel("product.get.request")

    _output_get_all = restapi.CerberusValidator({
         'data': {
                'type': 'list',
                'schema': {
                    'type': 'dict',
                    'schema': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'price': {'type': 'float'},
                    }
                }
             },
         'message': {'type': 'string'},
      })
    _output_create = restapi.CerberusValidator({
         'data': {
                'type': 'dict',
                'schema': {
                    'id': {'type': 'integer'},
                }
             },
         'message': {'type': 'string'},
      })
    _output_get_by_id = restapi.CerberusValidator({
         'data': {
                'type': 'dict',
                'schema': {
                    'id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'price': {'type': 'float'},
                }
             },
         'message': {'type': 'string'},
      })
    _output_update = restapi.CerberusValidator({
         'message': {'type': 'string'},
      })
    _output_delete = restapi.CerberusValidator({
         'message': {'type': 'string'},
      })
    
    @restapi.method(
        [(["/"], "GET")],
        input_param=_input_get_all,
        output_param=_output_get_all,
        auth="api_key"
    )
    def search(self, product_search_param):
        """
        Search for products
        """
        response = {}
        try:
            Product = self.env['product.model'].sudo()
            products = Product.getAll(product_search_param)
            response = {
                "message": "Products found" if products else "No products found",
                "data": products
            }
        except Exception as e:
            response = {
                "message": str(e),
                "data": []
            }
        return response
    
    @restapi.method(
        [(["/"], "POST")],
        input_param=_input_create,
        output_param=_output_create,
        auth="api_key"
    )
    def add(self, body):
        """
        Create product
        """
        response = {}
        try:
            Product = self.env['product.model'].sudo()
            new_product = Product.add(body.name, body.price)
            response = {
                "message": "Success" if new_product else "Failed",
                "data": new_product
            }
        except Exception as e:
            response = {
                "message": str(e),
                "data": {}
            }
        return response

    @restapi.method(
        [(["/<int:product_id>"], "GET")],
        output_param=_output_get_by_id,
        auth="api_key"
    )
    def get(self, product_id):
        """
        Get product by ID
        """
        response = {}
        try:
            Product = self.env['product.model'].sudo()
            product = Product.getById(product_id)
            response = {
                "message": "Product found" if product else "Product not found",
                "data": product
            }
        except Exception as e:
            response = {
                "message": str(e),
                "data": {}
            }
        return response

    @restapi.method(
        [(["/<int:product_id>"], "PUT")],
        input_param=_input_update,
        output_param=_output_update,
        auth="api_key"
    )
    def update(self, product_id, body):
        """
        Update product by ID
        """
        response = {}
        try:
            Product = self.env['product.model'].sudo()
            success = Product.update(product_id, body.name, body.price)
            response = {
                "message": "Product updated" if success else "Product not found",
            }
        except Exception as e:
            response = {
                "message": str(e),
            }
        return response

    @restapi.method(
        [(["/<int:product_id>"], "DELETE")],
        output_param=_output_delete,
        auth="api_key"
    )
    def delete(self, product_id):
        """
        Delete product by ID
        """
        response = {}
        try:
            Product = self.env['product.model'].sudo()
            success = Product.delete(product_id)
            response = {
                "message": "Product deleted" if success else "Product not found",
            }
        except Exception as e:
            response = {
                "message": str(e),
            }
        return response
