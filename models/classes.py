from odoo import fields, models

class Classes(models.Model):
    _name = 'fk.classes'
    _description = 'Classes'

    name = fields.Char(string='Title', required=True)
    division = fields.Char(string='Division', required=True)
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
    academic_year = fields.Char(string='Academic Year', required=True)
    course_id = fields.Many2one(
        'fk.course',
        string='Course',
        required=True
    )
    student_ids = fields.Many2many(
        'fk.student',
        string='Students'
    )
