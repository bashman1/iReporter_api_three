from flask import Flask, jsonify, request
from app.controllers.auth import Auth
from app.controllers.red_flags import ReportRedFlag


app = Flask(__name__)
auth = Auth()
redflag = ReportRedFlag()

# the index route

@app.route('/api/v1')
def index():
    return jsonify({"Message":"Welcome to iReporter API try again"}), 200

# the auth route starts here

@app.route('/api/v1/auth/signup', methods=['POST']) 
def user_registration():
    data = request.get_json()
    return auth.signup(data)
    # pass
    # return jsonify({"Message":"User registration"})

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    return auth.login(data)
    # return jsonify({"Message":"User LogIn"})

@app.route('/api/v1/users')
def fetcha_all_users():
    return jsonify({"users":auth.get_users()}), 200

# @app.route('/api/v1/checkuser')
# def find_users():
#     return auth.check_users()

@app.route('/api/v1/red-flags', methods=['POST'])
def repoting():
    data = request.get_json()
    return redflag.report_red_flag(data)

@app.route('/api/v1/red-flags')
def fetch_redflags():
    return jsonify({"Red-flag":redflag.fetch_all_red_flags()}), 200

@app.route('/api/v1/red-flags/<int:redflag_id>')
def get_specific_redflag(redflag_id):
    return redflag.fetch_specific_redflag(redflag_id)

@app.route('/api/v1/red-flags/<int:redflag_id>', methods=['DELETE'])
def delete_redflag(redflag_id):
    return redflag.delete_redflag(redflag_id), 200