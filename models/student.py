from odoo import fields, models

class Student(models.Model):
    _name = 'fk.student'
    _description = 'Student'

    roll_no = fields.Char(string='Roll No', required=True)
    name = fields.Char(string='Name', required=True)
    dob = fields.Date(string='Date of Birth')
    phone = fields.Char(string='Phone Number')
    batch_id = fields.Many2one('fk.batch', string='Batch')
    classes_ids = fields.Many2many(
        'fk.classes',
        string='class:'
    )
    # class_ids = fields.Many2many('university.class', string='Classes')
