from app.models import TimeExercisesTaxonomy
from app.service import TimeExercisesTaxonomyService

class TimeExercisesManagement(object):
    """
    Interactions with TimeExercises both Histories and Taxonomies

    I N T E R F A C E   G U A R AN T E E D
    --------------------------------------

    submit_taxonomy_entry(name):
        -- Creates and adds a TimeExercisesTaxonomy to the database. Returns the added entry
    """
    @staticmethod
    def submit_taxonomy_entry(name):
        entry_to_add = TimeExercisesTaxonomy(name=name)

        TimeExercisesTaxonomyService.add_entry_to_db(entry_to_add)

        return entry_to_add
