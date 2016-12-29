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


class RepExerciseTaxonomy(db.Model):
    __tablename__ = 'rep_exercise_taxonomy'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    is_back = db.Column(db.Boolean)
    is_chest = db.Column(db.Boolean)
    is_shoulders = db.Column(db.Boolean)
    is_biceps = db.Column(db.Boolean)
    is_triceps = db.Column(db.Boolean)
    is_legs = db.Column(db.Boolean)
    is_core = db.Column(db.Boolean)
    is_balance = db.Column(db.Boolean)
    is_cardio = db.Column(db.Boolean)
    is_weight_per_hand = db.Column(db.Boolean)

    def __init__(self, name, is_back, is_chest, is_shoulders, is_biceps, is_triceps, is_legs, is_core, is_balance,
                 is_cardio, is_weight_per_hand):
        self.name = name
        self.is_back = is_back
        self.is_chest = is_chest
        self.is_shoulders = is_shoulders
        self.is_biceps = is_biceps
        self.is_triceps = is_triceps
        self.is_legs = is_legs
        self.is_core = is_core
        self.is_balance = is_balance
        self.is_cardio = is_cardio
        self.is_weight_per_hand = is_weight_per_hand

    def __repr__(self):
        return '<{0}:  is_back: {1}  is_chest: {2}  is_shoulders: {3}  is_biceps: {4}  is_triceps: {5}  is_legs: {6}' \
               '  is_core: {7}  is_balance: {8}  is_cardio: {9}  is_weight_per_hand:  {10}>'\
            .format(
                self.name,
                self.is_back,
                self.is_chest,
                self.is_shoulders,
                self.is_biceps,
                self.is_triceps,
                self.is_legs,
                self.is_core,
                self.is_balance,
                self.is_cardio,
                self.is_weight_per_hand
            )
