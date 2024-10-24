from odoo import fields, models

class TTData(models.Model):
    _name = 'fk.timetable'
    _description = 'Classroom Schedule Data'

    name = fields.Char(string='Room', required=True)
    hour = fields.Char(string='Hour', required=True)
    day = fields.Selection(
        [
            ('monday', 'Monday'),
            ('tuesday', 'Tuesday'),
            ('wednesday', 'Wednesday'),
            ('thursday', 'Thursday'),
            ('friday', 'Friday'),
            ('saturday', 'Saturday'),
            ('sunday', 'Sunday')
        ],
        string='Day',
        required=True
    )
    classes_ids = fields.Many2many(
        'fk.classes',
        string='class:'
    )