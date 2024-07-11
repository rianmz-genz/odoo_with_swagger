from odoo import models, fields, api

class ProductModel(models.Model):
    _name = 'product.model'

    @api.model
    def add(self, name, price):
        Product = self.env['product.template'].sudo()
        new_product = Product.create({
            'name': name,
            'list_price': price
        })
        return {
            'id': new_product.id
        }

    @api.model
    def getAll(self, params):
        Product = self.env['product.template'].sudo()
        domain = []
        if params.name:
            domain.append(("name", "ilike", params.name))
        if params.id:
            domain.append(("id", "=", params.id))
            
        products = Product.search(domain)
        return [{
            'id': product.id,
            'name': product.name,
            'price': product.list_price
        } for product in products]

    @api.model
    def getById(self, product_id):
        Product = self.env['product.template'].sudo()
        product = Product.search([('id', '=', product_id)], limit=1)
        if product:
            return {
                'id': product.id,
                'name': product.name,
                'price': product.list_price
            }
        else:
            return {'error': 'Product not found'}

    @api.model
    def update(self, product_id, name=None, price=None):
        Product = self.env['product.template'].sudo()
        product = Product.search([('id', '=', product_id)], limit=1)
        if product:
            values = {}
            if name:
                values['name'] = name
            if price:
                values['list_price'] = price
            product.write(values)
            return {'success': True}
        else:
            return {'error': 'Product not found'}

    @api.model
    def delete(self, product_id):
        Product = self.env['product.template'].sudo()
        product = Product.search([('id', '=', product_id)], limit=1)
        if product:
            product.unlink()
            return {'success': True}
        else:
            return {'error': 'Product not found'}
