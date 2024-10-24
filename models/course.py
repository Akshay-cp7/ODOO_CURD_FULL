from odoo import fields, models

class Course(models.Model):
    _name = 'fk.course'
    _description = 'Course'

    name = fields.Char(string='Title', required=True)
    year_of_admission = fields.Integer(string='Year of Admission', required=True)
    level = fields.Selection(
        [('UG', 'UG'), ('PG', 'PG')],
        string='Level',
        required=True
    )
    course_code = fields.Char(string='Course Code', required=True)
    semester = fields.Selection(
        [(str(i), str(i)) for i in range(1, 11)],
        string='Semester',
        required=True
    )
    department_id = fields.Many2one(
        'fk.dept', 
        string='Department',
        required=True
    )
