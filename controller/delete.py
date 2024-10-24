from odoo import http
from odoo.http import request
import json

class DeleteFaculty(http.Controller):
    @http.route('/delete_faculty/<int:faculty_id>', auth='public', type='http', methods=['DELETE'], csrf=False)
    def delete_faculty(self, faculty_id):
        try:
            faculty_record = request.env['fk.faculty'].sudo().browse(faculty_id)
            if faculty_record.exists():
                faculty_record.unlink()
                return request.make_response(
                    json.dumps({'status': 'success', 'message': 'Faculty deleted successfully'}),
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
