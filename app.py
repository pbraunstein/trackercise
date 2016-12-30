import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import RepExercisesHistory, RepExercisesTaxonomy


@app.route('/')
def hello():
    results = db.engine.execute('select * from rep_exercises_history;')
    entries = list(results)
    entries = [_prepare_entry(x) for x in entries]
    return render_template('index.html', entries=entries)


def _prepare_entry(entry):
    values = entry.values()
    values[-1] = str(values[-1])
    return values


if __name__ == '__main__':
    app.run()
