from app import db


class RepExercisesHistory(db.Model):
    __tablename__ = 'rep_exercises_history'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String())
    name = db.Column(db.String())
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    weight = db.Column(db.Float)
    date = db.Column(db.DateTime)

    def __init__(self, user_id, name, sets, reps, weight, date):
        self.user_id = user_id
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.date = date

    def __repr__(self):
        return '<{0}: {1} sets of {2} reps at {3} lbs. on {4}>'.format(self.name, self.sets, self.reps, self.weight,
                                                                       self.date)