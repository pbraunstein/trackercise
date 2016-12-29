import os
from csv import reader

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db
from models import RepExerciseTaxonomy

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def run_importers():
    """
    Not yet implemented
    """
    import_rep_taxonomies()


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
                entries.append(RepExerciseTaxonomy(
                    row[0],
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


def _booleanize(yes_or_no):
    """
    Takes in the string YES or NO and booleanizes it

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


@manager.command
def import_rep_history():
    raise NotImplementedError("import_rep_history is not yet implemented")

if __name__ == '__main__':
    manager.run()
