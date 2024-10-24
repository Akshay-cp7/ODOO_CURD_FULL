from odoo import http
from odoo.http import request
import json

class FacultyController(http.Controller):
    @http.route('/create_faculty', auth='public', type='http', methods=['POST'], csrf=False)
    def create_faculty(self):
        try:
            # Get the JSON data from the request body
            faculty_data = json.loads(request.httprequest.data)

            # Create a new faculty record
            faculty_record = request.env['fk.faculty'].sudo().create({
                'name': faculty_data.get('name'),
                'code': faculty_data.get('code'),
            })

            return request.make_response(
                json.dumps({
                    'status': 'success',
                    'message': 'Faculty record created successfully',
                    'id': faculty_record.id  # Return the new ID
                }),
                headers={'Content-Type': 'application/json'}
            )
        except Exception as e:
            return request.make_response(
                json.dumps({'error': str(e)}),
                headers={'Content-Type': 'application/json'},
                status=500
            )