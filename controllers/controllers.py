# -*- coding: utf-8 -*-
# from odoo import http


# class Lv(http.Controller):
#     @http.route('/lv/lv', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lv/lv/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lv.listing', {
#             'root': '/lv/lv',
#             'objects': http.request.env['lv.lv'].search([]),
#         })

#     @http.route('/lv/lv/objects/<model("lv.lv"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lv.object', {
#             'object': obj
#         })
