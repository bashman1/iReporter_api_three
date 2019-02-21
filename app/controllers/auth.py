from flask import jsonify, request
from app.models.app_models import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Auth:

    def __init__(self):
        self.user_list = []

    def add_user(self, user):
        new_user = user.__dict__
        self.user_list.append(new_user)

    def get_users(self):
        return self.user_list

    def auto_generate_user_id(self):
        if len(self.user_list) == 0:
            return 1
        return len(self.user_list)+1

    
    # def check_users(self):
    #     for user in self.user_list:
    #         return dict(user)


    def signup(self, data):
        user_id = self.auto_generate_user_id()
        username = data['username']
        email = data['email']
        password = data['password']
        registered = datetime.now().strftime('%d/%h/%Y %H:%M')
        is_admin = data['is_admin']

        if not type(username) == str:
            return jsonify({'message':'Username must be a string'}), 400
        username = (username).strip()

        if not type(email) == str:
            return jsonify({'message':'Email must be a string'}), 400
        email = (email).strip()

        if not type(password) == str:
            return jsonify({'message':'Password must be a string'}), 400
        password=(password).strip()

        if not username.strip():
            return jsonify({'message':'Username cannot be empty'}), 400

        if not email.strip():
            return jsonify({'message':'Email cannot be empty'}), 400
        
        if not password.strip():
            return jsonify({'message':'Password cannot be empty'}), 400

        if len(username)<3:
            return jsonify({'message':'Username too short'}), 400

        if len(password)<5:
            return jsonify({'message':'Password too short'}), 400
        
        if not '@' in email:
            return jsonify({'message':'Invalid email format'}), 400

        
        # if self.check_users(['username']) == username:
        #     return jsonify({'message':'Username already registered'})

        

        password = generate_password_hash(password)

        new_user = User(user_id,username,email,password,registered,is_admin)
        self.add_user(new_user)

        return jsonify({'message':'User {} registered.'.format(username)}), 201


    def login(self, data):
        req_username = data['username']
        req_password = data['password']

        if not type(req_username) == str:
            return jsonify({'message':'Username must be a string'}), 400
        req_username = (req_username).strip()
        
        if not type(req_password) ==str:
            return jsonify({'message':'Password must be a string'}), 400
        req_password = (req_password).strip()

        for user in self.user_list:
            if user['username'] == req_username and check_password_hash(user['password'], req_password):
                return jsonify({'message':'User {} has logedin.'.format(req_username)}), 200
            # return jsonify({'message':'User is not registered'})
        return jsonify({'message':'No users found'}), 401


            
        
