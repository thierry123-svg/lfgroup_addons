from odoo import api, fields, models, SUPERUSER_ID, _

class Contact(models.Model):
    _inherit = 'res.partner'
    _description = "update info contact"

    cni_number = fields.Char(string='CNI Number', required=True)
    niu_number = fields.Char(string='NIU Number', help="Reference of the document that generated this sales order request.")
