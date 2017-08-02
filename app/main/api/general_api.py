from os.path import dirname, join
from json import dumps

from flask import send_file


from app.brain.admin.all_data import AllData
from app.brain.utilities import all_data_to_dict
from app.main import main_blueprint as main


@main.route('/')
def ts():
    serve_path = dirname(main.root_path)
    serve_path = join(serve_path, 'static')
    serve_path = join(serve_path, 'dist')
    serve_path = join(serve_path, 'index.html')
    return send_file(serve_path), 200


@main.route('/all-data', methods=['POST'])
def all_data():
    return dumps(all_data_to_dict(AllData.get_all_data())), 200

