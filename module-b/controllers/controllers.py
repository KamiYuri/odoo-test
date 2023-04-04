# -*- coding: utf-8 -*-
# from odoo import http


# class Module-b(http.Controller):
#     @http.route('/module-b/module-b', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module-b/module-b/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module-b.listing', {
#             'root': '/module-b/module-b',
#             'objects': http.request.env['module-b.module-b'].search([]),
#         })

#     @http.route('/module-b/module-b/objects/<model("module-b.module-b"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module-b.object', {
#             'object': obj
#         })
