{
    'name': 'Collage Management',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 10,
    'summary': 'Manage student information',
    'description': 'This module allows you to manage student information',
    'author': 'Akshay C P',
    'depends': ['base','mail'],
     'data': [
    'views/time_table_view.xml',#add comma before
    'views/tt_data_view.xml',
    'views/faculty_view.xml',
    'views/classes_view.xml',
    'views/course_view.xml',
    'views/dept_view.xml',
    'views/program_view.xml',
    'views/batch_view.xml',
    'views/student_view.xml',
    'views/menu.xml',
    ],
    'installable': True,
    'application': True,


}
