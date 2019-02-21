import json
from unittest import TestCase
from app.views.app_views import app

class ApiTest(TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.user_signup = {"user_id":1,"username":"bash","email":"bash@gmail.com","password":"password","registered":"1/2/2018","is_admin":0}
        self.user_login ={  
                            "username":"bash",
                            "password":"password"
                        }
        self.red_flag = {   
                            "created_by" : 1,
                            # "created_on": "18/Feb/2019 16:29",
                            "incident_type" : "red-flag",
                            "location" : "Kampala",
                            "status" : "Drafted",
                            "images" : "thhh.png" ,
                            "videos" : "videos.mp4",
                            "comment" : "This is a comment" 
                        }

    """testing the root page"""
    def test_index(self):
        response = self.client.get('/api/v1')
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup), 
                                    content_type ='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('bash', json.loads(response.data)['message'])

    def test_signup_email_format(self):
        self.user_signup['email']='bash.com'
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup), 
                                        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid email format', json.loads(response.data)['message'])

    def test_username_type(self):
        self.user_signup['username']=123
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup),
                                        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Username must be a string', json.loads(response.data)['message'])

    def test_password_type(self):
        self.user_signup['password']=123
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup),
                                        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Password must be a string', json.loads(response.data)['message'])

    def test_email_type(self):
        self.user_signup['email']=1235.78
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup),
                                        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Email must be a string', json.loads(response.data)['message'])

    def test_empty_username(self):
        self.user_signup['username']=''
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup),
                                        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Username cannot be empty', json.loads(response.data)['message'])

    def test_empty_email(self):
        self.user_signup['email']=''
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup),
                                        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Email cannot be empty', json.loads(response.data)['message'])

    def test_empty_password(self):
        self.user_signup['password']=''
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup),
                                        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Password cannot be empty', json.loads(response.data)['message'])

    def test_password_length(self):
        self.user_signup['password']='pa'
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup),
                                        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Password too short', json.loads(response.data)['message'])

    def test_username_length(self):
        self.user_signup['username']='ba'
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup),
                                        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Username too short', json.loads(response.data)['message'])

    def test_signin(self):
        self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup),
                            content_type = 'application/json')
        login_resp = self.client.post('/api/v1/auth/login', data=json.dumps(self.user_login),
                                        content_type ='application/json')
        self.assertEqual(login_resp.status_code, 200)

    def test_signin_username(self):
        self.user_login['username']= 12
        self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup),
                            content_type = 'application/json')
        login_resp = self.client.post('/api/v1/auth/login', data=json.dumps(self.user_login),
                                        content_type ='application/json')
        self.assertEqual(login_resp.status_code, 400)

    def test_signin_password(self):
        self.user_login['password'] = 56
        self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup),
                            content_type = 'application/json')
        login_resp = self.client.post('/api/v1/auth/login', data=json.dumps(self.user_login),
                                        content_type ='application/json')
        self.assertEqual(login_resp.status_code, 400)

    def test_user_not_found(self):
        self.user_login['username']='baash'
        self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup),
                            content_type = 'application/json')
        
        login_resp = self.client.post('/api/v1/auth/login', data=json.dumps(self.user_login),
                                        content_type ='application/json')
        self.assertEqual(login_resp.status_code, 401)
        self.assertIn('No users found', json.loads(login_resp.data)['message'])

    def test_get_users(self):
        self.client.post('/api/v1/auth/signup', data=json.dumps(self.user_signup),
                            content_type = 'application/json')
        get_users = self.client.get('/api/v1/users')
        self.assertEqual(get_users.status_code, 200)


        """ test the red-flags"""

    # def test_report_redflag(self):
    #     response = self.client.post('/api/v1/red-flags', json.dumps(self.red_flag),
    #                                 content_type='application/json')
    #     self.assertEqual(response.status_code, 400)
        
    def test_createdby_type(self):
        self.red_flag['created_by']='12'
        response = self.client.post('/api/v1/red-flags', json.dumps(self.red_flag),
                                    content_type='application/json')
        self.assertIn('created by must be a number', json.loads(response.data)['message'])

