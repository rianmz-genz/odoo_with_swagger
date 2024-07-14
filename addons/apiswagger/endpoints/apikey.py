from odoo.addons.base_rest import restapi
from odoo.addons.component.core import Component

class ProductNewApiService(Component):
    _inherit = "base.rest.service"
    _name = "apikey.new_api.service"
    _usage = "apikey"
    _collection = "base.public"
    _description = """
        List of Api Key
    """
    _default_auth = "public"
    
    _input_get_all = restapi.Datamodel("apikey.search.param")
    
    _output_get_all = restapi.CerberusValidator({
         'data': {
                'type': 'list',
                'schema': {
                    'type': 'dict',
                    'schema': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'user': {'type': 'string'},
                        'key': {'type': 'string'},
                    }
                }
             },
         'message': {'type': 'string'},
      })
    
    @restapi.method(
        [(["/"], "GET")],
        input_param=_input_get_all,
        output_param=_output_get_all,
        auth="public"
    )
    def search(self, params):
        """
        Search for apikeys
        """
        response = {}
        try:
            ApiKey = self.env['apikey.model'].sudo()
            apikeys = ApiKey.getAll(params)
            response = {
                "message": "ApiKeys found" if apikeys else "No apikeys found",
                "data": apikeys
            }
        except Exception as e:
            response = {
                "message": str(e),
                "data": []
            }
        return response