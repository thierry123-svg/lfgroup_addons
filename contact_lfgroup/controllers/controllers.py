# -*- coding: utf-8 -*-
# from odoo import http


# class ContactLfgroup(http.Controller):
#     @http.route('/contact_lfgroup/contact_lfgroup/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact_lfgroup/contact_lfgroup/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact_lfgroup.listing', {
#             'root': '/contact_lfgroup/contact_lfgroup',
#             'objects': http.request.env['contact_lfgroup.contact_lfgroup'].search([]),
#         })

#     @http.route('/contact_lfgroup/contact_lfgroup/objects/<model("contact_lfgroup.contact_lfgroup"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact_lfgroup.object', {
#             'object': obj
#         })
