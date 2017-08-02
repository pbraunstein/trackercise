from json import dumps

from flask import request, g, Response
from flask_login import current_user
from flask_wtf.csrf import generate_csrf

from app import csrf
from app.brain.admin.user_data import UserData
from app.brain.user_management.account_updater import AccountUpdater
from app.brain.user_management.change_password_result import ChangePasswordResult
from app.brain.user_management.loginerator import Loginerator
from app.brain.user_management.login_result import LoginResult
from app.brain.user_management.register_city import RegisterCity
from app.brain.user_management.register_result import RegisterResult
from app.brain.utilities import user_data_to_dict
from app.main import main_blueprint as main


@main.route('/status', methods=['GET', 'POST'])
def status():
    return dumps({'status': 'good'}), 200


@main.route('/user-data', methods=['POST'])
def user_data():
    csrf.protect()
    if not current_user.is_authenticated:
        return dumps({'status': 'bad'}), 400
    return dumps(user_data_to_dict(UserData.get_user_data())), 200


@main.route('/login', methods=['POST'])
def login():
    parameters = request.get_json()
    email = parameters.get('email')
    password = parameters.get('password')
    login_result = Loginerator.login(email, password)
    if login_result == LoginResult.LOGGED_IN:
        response = Response(dumps({
            'status': 'good',
            'user_logged_in': current_user.nickname
        }))
        generate_csrf()
        response.headers['X-CSRFToken'] = getattr(g, 'csrf_token')
        return response, 200
    else:
        return dumps({'status': 'bad'}), 400


@main.route('/who-am-i', methods=['POST'])
def who_am_i():
    if current_user.is_authenticated:
        return dumps({
            'user': current_user.nickname,
            'password': current_user.password
        }), 200
    else:
        return dumps({
            'user': ''
        }), 200


@main.route('/logout', methods=['POST'])
def logout():
    Loginerator.logout()
    return dumps({}), 200


@main.route('/register', methods=['POST'])
def register():
    parameters = request.get_json()
    email = parameters.get('email')
    nickname = parameters.get('nickname')
    password = parameters.get('password')
    reg_result = RegisterCity.register(email, nickname, password)
    if reg_result == RegisterResult.REGISTERED:
        return dumps({'status': 'good'}), 200
    else:
        return dumps({'status': 'bad'}), 400


@main.route('/change-password', methods=['POST'])
def change_password():
    if not current_user.is_authenticated:
        return dumps({'status': 'bad'}), 400

    parameters = request.get_json()
    old_password = parameters.get('old_password')
    new_password = parameters.get('new_password')
    confirm_password = parameters.get('confirm_password')
    change_password_result = AccountUpdater.change_password(old_password, new_password, confirm_password)

    if change_password_result == ChangePasswordResult.PASSWORD_CHANGE_SUCCESSFUL:
        return dumps({'status': 'good'}), 200
    else:
        return dumps({'status': 'bad'}), 400
