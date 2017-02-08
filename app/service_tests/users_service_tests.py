from app.models import Users
from app.service import UsersService
from app.service_tests.service_test_case import ServiceTestCase


class UsersServiceTests(ServiceTestCase):
    def test_add_user_to_database(self):
        test_email = 'jake@jake.jake'
        test_nickname = 'Jake'
        test_fake_hash_password = 'pass'

        UsersService.add_user_to_database(test_email, test_nickname, test_fake_hash_password)
        actual_user = list(Users.query.all())[0]

        self.assertEqual(actual_user.email, test_email)
        self.assertEqual(actual_user.nickname, test_nickname)
        self.assertEqual(actual_user.password, test_fake_hash_password)