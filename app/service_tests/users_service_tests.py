from app.models import Users
from app.service import UsersService
from app.service_tests.service_test_case import ServiceTestCase


class UsersServiceTests(ServiceTestCase):
    def test_add_user_to_database(self):
        expected_user = Users(email='jake@jake.jake',
                              nickname='Jake',
                              password='pass')

        UsersService.add_user_to_database(expected_user.email, expected_user.nickname, expected_user.password)
        actual_user = list(Users.query.all())[0]

        self.assertEqual(actual_user, expected_user)

    def test_user_with_email_already_exists_already_exists(self):
        pass

    def test_user_with_email_already_exists_does_not_exist(self):
        pass
