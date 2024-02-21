from odoo import api, fields, models, SUPERUSER_ID, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    cni_number = fields.Char(string='Cni Number', required=True)
    niu_number = fields.Char(string='NIU Number', required=True)