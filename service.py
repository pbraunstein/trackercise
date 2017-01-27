from app import db
from models import Users


class UsersService(object):
    @staticmethod
    def get_user_with_email(email):
        return db.session.query(Users).filter(Users.email == email).first()
