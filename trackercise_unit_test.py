import unittest

from app import create_app


class TrackerciseUnittestCase(unittest.TestCase):
    def setUp(self):
        super(TrackerciseUnittestCase, self).setUp()
        self.app = create_app('testing')
