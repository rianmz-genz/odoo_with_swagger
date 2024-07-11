# -*- coding: utf-8 -*-
from odoo.addons.base_rest.controllers import main

class PublicRest(main.RestController):
    _root_path = '/api/public/'
    _collection_name = "base.public"
    _default_auth = "public"

class PrivateRest(main.RestController):
    _root_path = '/api/private/'
    _collection_name = "base.private"
    _default_auth = "api_key"
