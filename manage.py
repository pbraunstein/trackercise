from csv import reader, writer
from datetime import date
import hashlib
import os
import subprocess

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import db, create_app
from app.constants import FILE_HANDLES
from app.models import Users, RepExercisesTaxonomy, RepExercisesHistory, TimeExercisesTaxonomy, TimeExercisesHistory

app = create_app(os.environ.get('APP_SETTINGS') or 'default')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# FILE PATH CONSTANTS
USERS_FILE_PATH = os.path.join(app.root_path,
                               FILE_HANDLES.USERS + FILE_HANDLES.SEPARATOR + str(date.today()) + FILE_HANDLES.EXTENSION)
REP_TAXONOMY_FILE_PATH = os.path.join(app.root_path, FILE_HANDLES.REP_TAXONOMY + FILE_HANDLES.SEPARATOR + str(
    date.today()) + FILE_HANDLES.EXTENSION)
REP_HISTORY_FILE_PATH = os.path.join(app.root_path, FILE_HANDLES.REP_HISTORY + FILE_HANDLES.SEPARATOR + str(
    date.today()) + FILE_HANDLES.EXTENSION)


@manager.command
def backup_data_to_s3():
    """
    Runs the exporters, uploads each of the files up to s3, and then deletes the files that were created
    """
    run_exporters()
    _upload_files_s3()
    _clean_up_from_export()


def _upload_files_s3():
    subprocess.call(['aws', 's3', 'cp', USERS_FILE_PATH, 's3://trackercise'])
    subprocess.call(['aws', 's3', 'cp', REP_TAXONOMY_FILE_PATH, 's3://trackercise'])
    subprocess.call(['aws', 's3', 'cp', REP_HISTORY_FILE_PATH, 's3://trackercise'])


def _clean_up_from_export():
    os.unlink(USERS_FILE_PATH)
    os.unlink(REP_TAXONOMY_FILE_PATH)
    os.unlink(REP_HISTORY_FILE_PATH)


@manager.command
def run_importers():
    """
    Import rep taxonomy and rep history
    """
    import_users()
    import_rep_taxonomies()
    import_time_taxonomies()
    import_rep_history()
    import_time_history()


@manager.command
def run_exporters():
    """
    Exports all db contents into three csv files
    """
    export_users()
    export_rep_taxonomies()
    export_time_taxonomies()
    export_rep_history()
    export_time_history()


@manager.command
def import_users():
    hasher = hashlib.sha256()
    hasher.update('a')
    password = hasher.hexdigest()
    user = Users(email='a@a.a', nickname='Phil', password=password)
    db.session.add(user)
    db.session.commit()


@manager.command
def export_users():
    """
    Exports the users from the db into a CSV file
    """
    users = Users.query.all()
    with open(USERS_FILE_PATH, 'w') as csvfile:
        user_writer = writer(csvfile)
        user_writer.writerow(Users.get_attribute_header_list())
        for u in users:
            user_writer.writerow(u.get_attribute_list())


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
def export_rep_taxonomies():
    """
    Exports the rep taxonomies from the db into a CSV file
    """
    taxonomies = RepExercisesTaxonomy.query.all()
    with open(REP_TAXONOMY_FILE_PATH, 'w') as csvfile:
        taxonomy_writer = writer(csvfile)
        taxonomy_writer.writerow(RepExercisesTaxonomy.get_attribute_header_list())
        for t in taxonomies:
            taxonomy_writer.writerow(t.get_attribute_list())


@manager.command
def import_time_taxonomies():
    pass


@manager.command
def export_time_taxonomies():
    """
    Exports the time taxonomies from the db into a CSV file
    """
    taxonomies = TimeExercisesTaxonomy.query.all()


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


@manager.command
def export_rep_history():
    """
    Exports the rep exercise history from the db into a csv file
    """
    history = RepExercisesHistory.query.all()
    with open(REP_HISTORY_FILE_PATH, 'w') as csvfile:
        history_writer = writer(csvfile)
        history_writer.writerow(RepExercisesHistory.get_attribute_header_list())
        for h in history:
            try:
                history_writer.writerow(h.get_attribute_list())
            except AttributeError:
                pass


@manager.command
def import_time_history():
    pass


@manager.command
def export_time_history():
    pass


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
