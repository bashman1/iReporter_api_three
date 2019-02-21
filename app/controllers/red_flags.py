from flask import jsonify
from app.models.app_models import RedFlag
from datetime import datetime


class ReportRedFlag():

    def __init__(self):
        self.red_flag_list = []


    def add_red_flag(self, red_flag):
        new_red_flag = red_flag.__dict__
        self.red_flag_list.append(new_red_flag), 201

    def fetch_all_red_flags(self):
        return self.red_flag_list

    def auto_generate_id(self):
        if len(self.red_flag_list) == 0:
            return 1
        return len(self.red_flag_list)+1


    def report_red_flag(self, data):
        
        incident_id = self.auto_generate_id()
        created_on = datetime.now().strftime('%d/%h/%Y %H:%M')
        created_by = data['created_by']
        incident_type = data['incident_type']
        location = data['location']
        status = data['status']
        images = data['images']
        videos = data['videos']
        comment = data['comment']

        """validation process begins here """

        """ validating the input type """
        if not type(created_by) == int:
            return jsonify({"message":"created by must be a number"}), 400
        elif created_by < 1:
            return jsonify({"message":"created_by cannot be negative"}), 400
        

        if not type(incident_type) == str:
            return jsonify({"message":"incident type must be a string"}), 400
        incident_type =(incident_type).strip()

        if not type(location) == str:
            return jsonify({"message":"location must be a string"}), 400
        location =(location).strip()

        if not type(status) == str:
            return jsonify({"message":"status must be a string"}), 400
        status =(status).strip()
        
        if not type(images) == str:
            return jsonify({"message":"images must be a string"}), 400
        images =(images).strip()

        if not type(videos) == str:
            return jsonify({"message":"videos must be a string"}), 400
        videos =(videos).strip()

        if not type(comment) == str:
            return jsonify({"message":"comment must be a string"}), 400
        comment =(comment).strip()

        """ validating empty string """
        if not incident_type.strip():
            return jsonify({"message":"incident type cannot be empty"}), 400
        # if not data['created_by']:
        #     return jsonify({"message":"created by cannot be empty"}), 400

        if not location.strip():
            return jsonify({"message":"location cannot be empty"}), 400

        if not status.strip():
            return jsonify({"message":"status cannot be empty"}), 400

        if not images.strip():
            return jsonify({"message":"images cannot be empty"}), 400

        if not videos.strip():
            return jsonify({"message":"videos cannot be empty"}), 400

        if not comment.strip():
            return jsonify({"message":"comment cannot be empty"}), 400

        new_red_flag = RedFlag(incident_id, created_on, created_by, incident_type, location, \
            status, images, videos, comment)
        self.add_red_flag(new_red_flag)
        return jsonify({"Red-flag":self.red_flag_list}), 201

    def fetch_specific_redflag(self, redflag_id):
        for redflag in self.red_flag_list:
            if redflag['incident_id'] == redflag_id:
                return jsonify({"Red-flag":redflag}), 200
            # return jsonify({"message":"red-flag not found"}), 200
        return jsonify({"message":"No red-flags found"}), 200

    def delete_redflag(self, redflag_id):
        for redflag in self.red_flag_list:
            if redflag['incident_id'] == redflag_id:
                self.red_flag_list.remove(redflag)
                return jsonify({"message":"Red-flag id is deleted"}), 200
        return jsonify({"message":"no red-flags found"}), 200
        


    