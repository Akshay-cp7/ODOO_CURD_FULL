from odoo import fields, models

class Timetable(models.Model):
    _name = 'fk.timetbl'
    _description = 'Classroom Schedule Data'

    name = fields.Char(string='Year', required=True)
    start = fields.Char(string='Start', required=True)
    end = fields.Char(string='End', required=True)
    semester = fields.Selection(
        [(str(i), str(i)) for i in range(1, 11)],
        string='Semester',
        required=True
    )
    level = fields.Selection(
        [('UG', 'UG'), ('PG', 'PG')],
        string='Level',
        required=True
    )
    
    