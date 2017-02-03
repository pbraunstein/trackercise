import hashlib
import os
from csv import reader

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import db, create_app
from app.models import Users, RepExercisesTaxonomy, RepExercisesHistory

app = create_app(os.environ.get('APP_SETTINGS') or 'default')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def run_importers():
    """
    Import rep taxonomy and rep history
    """
    import_users()
    import_rep_taxonomies()
    import_rep_history()


@manager.command
def import_users():
    hasher = hashlib.sha256()
    hasher.update('a')
    password = hasher.hexdigest()
    user = Users(email='a@a.a', nickname='Phil', password=password)
    db.session.add(user)
    db.session.commit()


@manager.command
def import_rep_taxonomies():
    """
    Imports sample rep taxonomy data into the rep_exercise_taxonomy table

    Depends on the different ordering in the google drive file and the table columns. TODO: Very fragile
    """
    entries = []
    with open(os.path.join(app.root_path, 'sample_data/rep_taxonomy.csv'), 'rb') as csvfile:
        taxonomy_reader = reader(csvfile)
        taxonomy_reader.next()  # skip header line
        for row in taxonomy_reader:
            try:
                entries.append(RepExercisesTaxonomy(
                    row[0].upper(),
                    _booleanize(row[1]),
                    _booleanize(row[2]),
                    _booleanize(row[3]),
                    _booleanize(row[4]),
                    _booleanize(row[5]),
                    _booleanize(row[7]),
                    _booleanize(row[6]),
                    _booleanize(row[10]),
                    _booleanize(row[9]),
                    _booleanize(row[8]),
                ))
            except ValueError:
                pass
    db.session.add_all(entries)
    db.session.commit()


@manager.command
def import_rep_history():
    """
    Imports the rep exercise history sample data into the rep_exercises_history db table
    """
    entries = []
    user = Users.query.first()
    user_id = user.id
    with open(os.path.join(app.root_path, 'sample_data/rep_history.csv'), 'rb') as csvfile:
        history_reader = reader(csvfile)
        history_reader.next()  # skip header line
        for row in history_reader:
            entries.append(_generate_rep_history_from_row(row, user_id))
    db.session.add_all(entries)
    db.session.commit()


def _booleanize(yes_or_no):
    """
    Takes in the string YES or NO and booleanizes it to True of False

    :param yes_or_no: the string to booleanize
    :return: the boolean
    """
    yes_or_no = yes_or_no.upper()
    if yes_or_no == 'YES':
        return True
    elif yes_or_no == 'NO':
        return False
    else:
        raise ValueError("{0} is not a yes or no".format(yes_or_no))


def _generate_rep_history_from_row(row, user_id):
    """
    Generates a RepExercisesHistory object from one row of the csv file

    !!! Raises ValueError
    :param row: from csv sample data for rep exercises history csv file
    :param user_id: id of user
    :return: RepExercisesHistory taxonomy object representing one row in the db table
    """
    # if weight is body weight, signal that with -1
    if row[3] == 'body':
        row[3] = '-1'

    return RepExercisesHistory(
        user_id=user_id,
        exercise_id=_get_exercise_id_for_name(row[0]),
        sets=int(row[1]),
        reps=int(row[2]),
        weight=float(row[3]),
        date=row[4]
    )


def _get_exercise_id_for_name(exercise_name):
    """
    Gets the id of an exercise in the rep_exercises_taxonomy table

    !!! Throws TypeError

    :param exercise_name: name of exercise to look up
    :return: id of exercise in rep_exercises_taxonomy table
    """
    exercise_name = exercise_name.upper()
    result = RepExercisesTaxonomy.query.filter_by(name=exercise_name).first()
    if result is None:
        raise TypeError("No types match: {0} row is {1}".format(exercise_name))
    return result.id

if __name__ == '__main__':
    manager.run()
