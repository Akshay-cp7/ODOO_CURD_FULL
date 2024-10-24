from odoo import fields, models

class Program(models.Model):
    _name = 'fk.program'
    _description = 'Program'

    name = fields.Char(string='Title', required=True)
    level = fields.Selection(
        [('UG', 'UG'), ('PG', 'PG')],
        string='Level',
        required=True
    )
    is_self = fields.Boolean(string='Self', default=False)
    duration = fields.Integer(string='Duration (in hours)', required=True)
    department_id = fields.Many2one(
        'fk.dept', 
        string='Department'
    )
