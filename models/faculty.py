from odoo import fields, models

class Faculty(models.Model):
    _name = 'fk.faculty'
    _description = 'Faculty'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code')
    dept_id = fields.Many2one(
        'fk.dept', 
        string='Department', 
    )
