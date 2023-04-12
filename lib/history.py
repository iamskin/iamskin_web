import os
from flask import request, json

import globals
from lib import database

def serve(server):
    @server.route("/History", methods=["POST"])
    def get_history():
        uid = request.form.get('uid')
        rows = database.get_history(uid)

        # Json response format.
        response = json.jsonify(
            [
                {
                    "service_type": globals.config['chinese'][service_type]['normal'],
                    "upload_time": upload_time,
                    "upload_url": f"https://{globals.config['domain_name']}/assets/web/upload/{service_type}/{uid}/{upload_time}/{file_name}",
                    "output_url": f"https://{globals.config['domain_name']}/assets/web/predict/{service_type}/{uid}/{upload_time}/{file_name}"
                }
                for service_type, upload_time, file_name in rows
            ]
        )
        return response
    
    return server