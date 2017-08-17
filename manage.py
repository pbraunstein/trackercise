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

# EXPORT FILE PATH CONSTANTS
EXPORT_USERS_FILE_PATH = os.path.join(app.root_path, FILE_HANDLES.USERS + FILE_HANDLES.SEPARATOR + str(
    date.today()) + FILE_HANDLES.EXTENSION)
EXPORT_REP_TAXONOMY_FILE_PATH = os.path.join(app.root_path, FILE_HANDLES.REP_TAXONOMY + FILE_HANDLES.SEPARATOR + str(
    date.today()) + FILE_HANDLES.EXTENSION)
EXPORT_REP_HISTORY_FILE_PATH = os.path.join(app.root_path, FILE_HANDLES.REP_HISTORY + FILE_HANDLES.SEPARATOR + str(
    date.today()) + FILE_HANDLES.EXTENSION)
EXPORT_TIME_TAXONOMY_FILE_PATH = os.path.join(app.root_path, FILE_HANDLES.TIME_TAXONOMY + FILE_HANDLES.SEPARATOR + str(
    date.today()) + FILE_HANDLES.EXTENSION)
EXPORT_TIME_HISTORY_FILE_PATH = os.path.join(app.root_path, FILE_HANDLES.TIME_HISTORY + FILE_HANDLES.SEPARATOR + str(
    date.today()) + FILE_HANDLES.EXTENSION)

EXPORT_FILE_PATHS_MODELS_MAP = {
    EXPORT_USERS_FILE_PATH: Users,
    EXPORT_REP_TAXONOMY_FILE_PATH: RepExercisesTaxonomy,
    EXPORT_REP_HISTORY_FILE_PATH: RepExercisesHistory,
    EXPORT_TIME_TAXONOMY_FILE_PATH: TimeExercisesTaxonomy,
    EXPORT_TIME_HISTORY_FILE_PATH: TimeExercisesHistory
}

# IMPORT FILE PATH CONSTANTS
IMPORT_USERS_FILE_PATH = os.path.join(
    app.root_path,
    FILE_HANDLES.SAMPLE_DATA_DIR,
    FILE_HANDLES.USERS + FILE_HANDLES.EXTENSION
)
IMPORT_REP_TAXONOMY_FILE_PATH = os.path.join(
    app.root_path,
    FILE_HANDLES.SAMPLE_DATA_DIR,
    FILE_HANDLES.REP_TAXONOMY + FILE_HANDLES.EXTENSION
)
IMPORT_REP_HISTORY_FILE_PATH = os.path.join(
    app.root_path,
    FILE_HANDLES.SAMPLE_DATA_DIR,
    FILE_HANDLES.REP_HISTORY + FILE_HANDLES.EXTENSION
)
IMPORT_TIME_TAXONOMY_FILE_PATH = os.path.join(
    app.root_path,
    FILE_HANDLES.SAMPLE_DATA_DIR,
    FILE_HANDLES.TIME_TAXONOMY + FILE_HANDLES.EXTENSION
)
IMPORT_TIME_HISTORY_FILE_PATH = os.path.join(
    app.root_path,
    FILE_HANDLES.SAMPLE_DATA_DIR,
    FILE_HANDLES.TIME_HISTORY + FILE_HANDLES.EXTENSION
)


@manager.command
def backup_data_to_s3():
    """
    Runs the exporters, uploads each of the files up to s3, and then deletes the files that were created
    """
    run_exporters()
    _upload_files_s3()
    _clean_up_from_export()


def _upload_files_s3():
    for file_path in EXPORT_FILE_PATHS_MODELS_MAP.keys():
        subprocess.call(['aws', 's3', 'cp', file_path, 's3://trackercise'])


def _clean_up_from_export():
    for file_path in EXPORT_FILE_PATHS_MODELS_MAP.keys():
        os.unlink(file_path)


@manager.command
def run_importers():
    """
    Import rep taxonomy and rep history
    """
    import_users()
    import_rep_taxonomies()
    # import_time_taxonomies()
    import_rep_history()
    # import_time_history()


@manager.command
def run_exporters():
    for file_path, model in EXPORT_FILE_PATHS_MODELS_MAP.iteritems():
        export_model(file_path, model)


def export_model(file_path, model):
    data = model.query.all()
    with open(file_path, 'w') as csvfile:
        data_writer = writer(csvfile)
        data_writer.writerow(model.get_attribute_header_list())
        for d in data:
            try:
                data_writer.writerow(d.get_attribute_list())
            except:  # messy but it works
                pass


@manager.command
def import_users():
    entries = []
    with open(IMPORT_USERS_FILE_PATH, 'rb') as csvfile:
        users_reader = reader(csvfile)
        users_reader.next()  # skip the header line
        for row in users_reader:
            try:
                row = row[1:]  # remove previous row id
                entries.append(
                    Users(
                        email=row[0],
                        nickname=row[1],
                        password=row[2]
                    )
                )
            except:  # messy but effective
                pass
    db.session.add_all(entries)
    db.session.commit()


@manager.command
def import_rep_taxonomies():
    """
    Imports sample rep taxonomy data into the rep_exercise_taxonomy table
    """
    entries = []
    with open(IMPORT_REP_TAXONOMY_FILE_PATH, 'rb') as csvfile:
        taxonomy_reader = reader(csvfile)
        taxonomy_reader.next()  # skip header line
        for row in taxonomy_reader:
            try:
                row = row[1:]  # remove the previous row id that was in the table
                entries.append(RepExercisesTaxonomy(
                    row[0].upper(),
                    _string_to_bool(row[1]),
                    _string_to_bool(row[2]),
                    _string_to_bool(row[3]),
                    _string_to_bool(row[4]),
                    _string_to_bool(row[5]),
                    _string_to_bool(row[7]),
                    _string_to_bool(row[6]),
                    _string_to_bool(row[10]),
                    _string_to_bool(row[9]),
                    _string_to_bool(row[8]),
                ))
            except:  # messy but effective
                pass
    db.session.add_all(entries)
    db.session.commit()


@manager.command
def import_time_taxonomies():
    pass


@manager.command
def import_rep_history():
    """
    Imports the rep exercise history sample data into the rep_exercises_history db table
    """
    entries = []
    user = Users.query.first()
    with open(IMPORT_REP_HISTORY_FILE_PATH, 'rb') as csvfile:
        history_reader = reader(csvfile)
        history_reader.next()  # skip header line
        for row in history_reader:
            row = row[1:]
            try:
                entries.append(
                    RepExercisesHistory(
                        user_id=int(row[0]),
                        exercise_id=int(row[1]),
                        sets=int(row[2]),
                        reps=int(row[3]),
                        weight=float(row[4]),
                        date=row[5]
                    )
                )
            except:  # messy but effective
                pass
    db.session.add_all(entries)
    db.session.commit()


@manager.command
def export_rep_history():
    """
    Exports the rep exercise history from the db into a csv file
    """
    history = RepExercisesHistory.query.all()
    with open(EXPORT_REP_HISTORY_FILE_PATH, 'w') as csvfile:
        history_writer = writer(csvfile)
        history_writer.writerow(RepExercisesHistory.get_attribute_header_list())
        for h in history:
            try:
                history_writer.writerow(h.get_attribute_list())
            except:  # messy but effective
                pass


@manager.command
def import_time_history():
    pass


def _string_to_bool(string):
    if string.upper() == 'TRUE':
        return True
    else:
        return False


if __name__ == '__main__':
    manager.run()
