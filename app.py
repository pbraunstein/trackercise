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
    results_1 = RepExercisesHistory.query.all()
    entries_1 = list(results_1)
    entries_1 = [_prepare_entry(x) for x in entries_1]
    results_2 = db.engine.execute('select * from rep_exercises_taxonomy;')
    entries_2 = list(results_2)
    entries_2a = [list(x) for x in entries_2]
    entries_2b = [_prepare_taxonomy_entry(x) for x in entries_2a]
    entries = [entries_1, entries_2b]
    return render_template('index.html', entries=entries)


def _prepare_entry(entry):
    entry.date = str(entry.date)
    return entry


def _prepare_taxonomy_entry(entry):
    def filter_subentry(x):
        if type(x) == int:
            return x
        elif x == True:
            return 'YES'
        elif x == False:
            return 'NO'
        else:
            return x

    return [filter_subentry(x) for x in entry]



if __name__ == '__main__':
    app.run()
