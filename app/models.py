from sqlalchemy import ForeignKey

from app import db
from app import login_manager


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

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.name == other.name and
                self.is_back == other.is_back and
                self.is_chest == other.is_chest and
                self.is_shoulders == other.is_shoulders and
                self.is_biceps == other.is_biceps and
                self.is_triceps == other.is_triceps and
                self.is_legs == other.is_legs and
                self.is_core == other.is_core and
                self.is_balance == other.is_balance and
                self.is_cardio == other.is_cardio and
                self.is_weight_per_hand == other.is_weight_per_hand)

    def __ne__(self, other):
        return not self.__eq__(other)

    @classmethod
    def get_attribute_header_list(cls):
        return ['id', 'name', 'is_back', 'is_chest', 'is_shoulders', 'is_biceps', 'is_triceps', 'is_legs', 'is_core',
                'is_balance', 'is_cardio', 'is_weight_per_hand']

    def get_attribute_list(self):
        return [self.id, self.name, self.is_back, self.is_chest, self.is_shoulders, self.is_biceps, self.is_triceps,
                self.is_legs, self.is_core, self.is_balance, self.is_cardio, self.is_weight_per_hand]

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

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    nickname = db.Column(db.String(), nullable=False)
    password = db.Column(db.String())
    authenticated = db.Column(db.Boolean)

    def __init__(self, email, nickname, password):
        self.email = email
        self.nickname = nickname
        self.password = password
        self.authenticated = False  # all users start out not authenticated

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.email == other.email and
                self.nickname == other.nickname and
                self.password == other.password)

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_active(self):
        """All users are active"""
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        """No users can be anonymous"""
        return False

    @classmethod
    def get_attribute_header_list(cls):
        return ['id', 'email', 'nickname', 'password', 'authenticated']

    def get_attribute_list(self):
        return [self.id, self.email, self.nickname, self.password, self.authenticated]

    def __repr__(self):
        return '<Member Email: {0}  Nickname: {1}>'.format(self.email, self.nickname)


class RepExercisesHistory(db.Model):
    __tablename__ = 'rep_exercises_history'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    exercise_id = db.Column(db.Integer, ForeignKey('rep_exercises_taxonomy.id'), nullable=False)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    weight = db.Column(db.Float)
    date = db.Column(db.DateTime)

    def __init__(self, user_id, exercise_id, sets, reps, weight, date):
        self.user_id = user_id
        self.exercise_id = exercise_id
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.date = date

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.user_id == other.user_id and
                self.exercise_id == other.exercise_id and
                self.sets == other.sets and
                self.reps == other.reps and
                self.weight == other.weight and
                self.date == other.date)

    def __ne__(self, other):
        return not self.__eq__(other)

    @classmethod
    def get_attribute_header_list(cls):
        return ['id', 'user_id', 'exercise_id', 'sets', 'reps', 'weight', 'date']

    def get_attribute_list(self):
        return [self.id, self.user_id, self.exercise_id, self.sets, self.reps, self.weight,
                self.date.strftime('%Y-%m-%d')]

    def __repr__(self):
        return '<user_id: {0} exercise_id{1}: {2} sets of {3} reps at {4} lbs. on {5}>'.format(
            self.user_id, self.exercise_id, self.sets, self.reps, self.weight, self.date
        )


class TimeExercisesTaxonomy(db.Model):
    __tablename__ = 'time_exercises_taxonomy'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return '<name: {0}>'.format(self.name)


class TimeExercisesHistory(db.Model):
    __tablename__ = 'time_exercises_history'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    exercise_id = db.Column(db.Integer, ForeignKey('time_exercises_taxonomy.id'))
    distance = db.Column(db.Float)
    duration = db.Column(db.Integer)
    exercise_date = db.Column(db.DateTime)

    def __init__(self, user_id, exercise_id, distance, duration, exercise_date):
        self.user_id = user_id
        self.exercise_id = exercise_id
        self.distance = distance
        self.duration = duration
        self.exercise_date = exercise_date

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.user_id == other.user_id and
                self.exercise_id == other.exercise_id and
                self.distance == other.distance and
                self.duration == other.duration and
                self.exercise_date == other.exercise_date)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return '<user_id: {0} exercise_id: {1}; {2} distance in {3} time>'.format(
            self.user_id, self.exercise_id, self.distance, self.duration
        )


@login_manager.user_loader
def user_loader(user_email):
    return Users.query.get(user_email)
