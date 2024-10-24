from odoo import fields, models

class Batch(models.Model):
    _name = 'fk.batch'
    _description = 'Batch'

    name = fields.Char(string='Title', required=True)
    start_year = fields.Integer(string='Start Year', required=True)
    semester = fields.Integer(string='Semester', required=True)
    coordinator = fields.Char(string='Coordinator')
    program_id = fields.Many2one(
        'fk.program', 
        string='Program', 
        required=True
    )

    # programme_id = fields.Many2one('university.programme', string='Programme')
    # student_ids = fields.One2many('university.student', 'batch_id', string='Students')
