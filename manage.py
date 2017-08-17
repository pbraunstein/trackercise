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


def _generate_user_from_row(row):
    return Users(
        email=row[0],
        nickname=row[1],
        password=row[2]
    )


def _generate_rep_taxonomy_from_row(row):
    return RepExercisesTaxonomy(
        name=row[0].upper(),
        is_back=_string_to_bool(row[1]),
        is_chest=_string_to_bool(row[2]),
        is_shoulders=_string_to_bool(row[3]),
        is_biceps=_string_to_bool(row[4]),
        is_triceps=_string_to_bool(row[5]),
        is_legs=_string_to_bool(row[6]),
        is_core=_string_to_bool(row[7]),
        is_balance=_string_to_bool(row[8]),
        is_cardio=_string_to_bool(row[9]),
        is_weight_per_hand=_string_to_bool(row[10])
    )


def _generate_rep_history_from_row(row):
    return RepExercisesHistory(
        user_id=int(row[0]),
        exercise_id=int(row[1]),
        sets=int(row[2]),
        reps=int(row[3]),
        weight=float(row[4]),
        date=row[5]
    )


def _generate_time_taxonomy_from_row(row):
    return TimeExercisesTaxonomy(
        row[0].upper()
    )


def _generate_time_history_from_row(row):
    return TimeExercisesHistory(
        user_id=int(row[0]),
        exercise_id=int(row[1]),
        distance=float(row[2]),
        duration=int(row[3]),
        exercise_date=row[4]
    )

IMPORT_FILE_PATHS_FACTORY_METHOD_MAP = {
    IMPORT_USERS_FILE_PATH: _generate_user_from_row,
    IMPORT_REP_TAXONOMY_FILE_PATH: _generate_rep_taxonomy_from_row,
    IMPORT_REP_HISTORY_FILE_PATH: _generate_rep_history_from_row,
    IMPORT_TIME_TAXONOMY_FILE_PATH: _generate_time_taxonomy_from_row,
    IMPORT_TIME_HISTORY_FILE_PATH: _generate_time_history_from_row
}


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
    import_model(IMPORT_USERS_FILE_PATH, IMPORT_FILE_PATHS_FACTORY_METHOD_MAP[IMPORT_USERS_FILE_PATH])
    import_model(IMPORT_REP_TAXONOMY_FILE_PATH, IMPORT_FILE_PATHS_FACTORY_METHOD_MAP[IMPORT_REP_TAXONOMY_FILE_PATH])
    import_model(IMPORT_REP_HISTORY_FILE_PATH, IMPORT_FILE_PATHS_FACTORY_METHOD_MAP[IMPORT_REP_HISTORY_FILE_PATH])
    import_model(IMPORT_TIME_TAXONOMY_FILE_PATH, IMPORT_FILE_PATHS_FACTORY_METHOD_MAP[IMPORT_TIME_TAXONOMY_FILE_PATH])
    import_model(IMPORT_TIME_HISTORY_FILE_PATH, IMPORT_FILE_PATHS_FACTORY_METHOD_MAP[IMPORT_TIME_HISTORY_FILE_PATH])


@manager.command
def run_exporters():
    for file_path, model in EXPORT_FILE_PATHS_MODELS_MAP.iteritems():
        export_model(file_path, model)


def import_model(file_path, factory_method):
    entries = []
    with open(file_path, 'rb') as csvfile:
        data_reader = reader(csvfile)
        data_reader.next()  # skip header line

        for row in data_reader:
            try:
                row = row[1:]  # remove previous row id
                entries.append(
                    factory_method(row)
                )
            except:  # messy but effective
                pass
    db.session.add_all(entries)
    db.session.commit()


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


def _string_to_bool(string):
    if string.upper() == 'TRUE':
        return True
    else:
        return False


if __name__ == '__main__':
    manager.run()
