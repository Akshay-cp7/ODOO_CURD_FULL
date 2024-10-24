from odoo import fields, models

class Department(models.Model):
    _name = 'fk.dept'
    _description = 'Department'

    name = fields.Char(string='Department Name', required=True)
    is_self = fields.Boolean(string='Self', default=False)
