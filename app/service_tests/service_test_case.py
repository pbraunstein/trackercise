import unittest

from app import create_app, db


class ServiceTestCase(unittest.TestCase):
    def setUp(self):
        super(ServiceTestCase, self).setUp()
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        super(ServiceTestCase, self).tearDown()
        db.session.commit()
        db.drop_all()
        self.app_context.pop()
