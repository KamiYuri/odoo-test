# -*- coding: utf-8 -*-
# from odoo import http


# class Zalo-client(http.Controller):
#     @http.route('/zalo-client/zalo-client', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zalo-client/zalo-client/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zalo-client.listing', {
#             'root': '/zalo-client/zalo-client',
#             'objects': http.request.env['zalo-client.zalo-client'].search([]),
#         })

#     @http.route('/zalo-client/zalo-client/objects/<model("zalo-client.zalo-client"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zalo-client.object', {
#             'object': obj
#         })
