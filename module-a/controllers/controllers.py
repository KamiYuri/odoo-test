# -*- coding: utf-8 -*-
# from odoo import http


# class Module-a(http.Controller):
#     @http.route('/module-a/module-a', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module-a/module-a/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module-a.listing', {
#             'root': '/module-a/module-a',
#             'objects': http.request.env['module-a.module-a'].search([]),
#         })

#     @http.route('/module-a/module-a/objects/<model("module-a.module-a"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module-a.object', {
#             'object': obj
#         })
