from sqlalchemy import ForeignKey

from app import db


class RepExercisesTaxonomy(db.Model):
    __tablename__ = 'rep_exercises_taxonomy'

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


class Users(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(), primary_key=True, unique=True)
    nickname = db.Column(db.String(), nullable=False)
    password = db.Column(db.String())
    authenticated = db.Column(db.Boolean)

    def __init__(self, email, nickname, password):
        self.email = email
        self.nickname = nickname
        self.password = password
        self.authenticated = False  # all users start out not authenticated

    def is_active(self):
        """All users are active"""
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        """No users can be anonymous"""
        return False

    def __repr__(self):
        return '<Member Email: {0}  Nickname: {1}>'.format(self.email, self.nickname)


class RepExercisesHistory(db.Model):
    __tablename__ = 'rep_exercises_history'

    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(), ForeignKey('users.email'), nullable=False)
    exercise_id = db.Column(db.Integer, ForeignKey('rep_exercises_taxonomy.id'), nullable=False)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    weight = db.Column(db.Float)
    date = db.Column(db.DateTime)

    def __init__(self, user_email, exercise_id, sets, reps, weight, date):
        self.user_email = user_email
        self.exercise_id = exercise_id
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.date = date

    def __repr__(self):
        return '<{0}: {1} sets of {2} reps at {3} lbs. on {4}>'.format(self.exercise_id, self.sets, self.reps,
                                                                       self.weight, self.date)
