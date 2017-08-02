from flask import Blueprint

main_blueprint = Blueprint('main_blueprint', __name__)

from app.main.api import general_api
from app.main.api import rep_exercises_api
from app.main.api import time_exercises_api
from app.main.api import users_api
