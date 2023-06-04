# -*- coding: utf-8 -*-
# from odoo import http


# class ExcelTransformerTest(http.Controller):
#     @http.route('/excel_transformer_test/excel_transformer_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/excel_transformer_test/excel_transformer_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('excel_transformer_test.listing', {
#             'root': '/excel_transformer_test/excel_transformer_test',
#             'objects': http.request.env['excel_transformer_test.excel_transformer_test'].search([]),
#         })

#     @http.route('/excel_transformer_test/excel_transformer_test/objects/<model("excel_transformer_test.excel_transformer_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('excel_transformer_test.object', {
#             'object': obj
#         })
