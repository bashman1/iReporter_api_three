class User():


    def __init__(self, user_id, username, email, password, registered, is_admin):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.registered = registered
        self.is_admin = is_admin


class RedFlag():


    def __init__(self, incident_id, created_on, created_by, incident_type, location, \
                status, images, videos, comment):
        self.incident_id = incident_id
        self.created_on = created_on
        self.created_by = created_by
        self.incident_type = incident_type
        self.location = location
        self.status = status
        self.images = images 
        self.videos = videos
        self.comment = comment