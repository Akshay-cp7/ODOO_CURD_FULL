from odoo import http
from odoo.http import request
import json

class EditFaculty(http.Controller):
    @http.route('/edit_facultyk/<int:faculty_id>', auth='public', type='http', methods=['PUT'], csrf=False)
    def edit_faculty(self, faculty_id):
        try:
            # Get the JSON data from the request body
            faculty_data = json.loads(request.httprequest.data)

            # Get the faculty record based on the provided ID
            faculty_record = request.env['fk.faculty'].sudo().browse(faculty_id)

            # Check if the faculty record exists
            if faculty_record.exists():
                # Update the faculty record with the provided data
                faculty_record.write({
                    'name': faculty_data.get('name'),
                    'code': faculty_data.get('code')
                })

                return request.make_response(
                    json.dumps({'status': 'success', 'message': 'Faculty record updated successfully'}),
                    headers={'Content-Type': 'application/json'}
                )
            else:
                return request.make_response(
                    json.dumps({'error': 'Faculty not found'}),
                    headers={'Content-Type': 'application/json'},
                    status=404
                )
        except Exception as e:
            return request.make_response(
                json.dumps({'error': str(e)}),
                headers={'Content-Type': 'application/json'},
                status=500
            )
