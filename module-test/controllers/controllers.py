# -*- coding: utf-8 -*-
# from odoo import http


# class Module-test(http.Controller):
#     @http.route('/module-test/module-test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module-test/module-test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module-test.listing', {
#             'root': '/module-test/module-test',
#             'objects': http.request.env['module-test.module-test'].search([]),
#         })

#     @http.route('/module-test/module-test/objects/<model("module-test.module-test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module-test.object', {
#             'object': obj
#         })
