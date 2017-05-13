from app.models import Users
from app.service import UsersService
from app.service_tests.service_test_case import ServiceTestCase


class UsersServiceTests(ServiceTestCase):
    # mark_user_as_authenticated tests #
    def test_mark_user_as_authenticated(self):
        email='phil@phil.phil'
        user = Users(
            email=email,
            nickname='phil',
            password='pass'
        )
        UsersService.add_user_to_database(user)

        UsersService.mark_user_as_authenticated(user)

        user_again = UsersService.get_user_with_email(email)

        self.assertTrue(user_again.authenticated)

    # mark_user_as_not_authenticated tests #
    def test_mark_user_as_not_authenticated(self):
        email='phil@phil.phil'
        user = Users(
            email=email,
            nickname='phil',
            password='pass'
        )
        UsersService.add_user_to_database(user)

        UsersService.mark_user_as_authenticated(user)

        user_again = UsersService.get_user_with_email(email)

        self.assertTrue(user_again.authenticated)  # need to make sure user gets authenticated in the first place

        UsersService.mark_user_as_not_authenticated(user_again)

        users_again_again = UsersService.get_user_with_email(email)

        self.assertFalse(users_again_again.authenticated)

    # add_user_to_database tests #
    def test_add_user_to_database(self):
        expected_user = Users(email='jake@jake.jake',
                              nickname='Jake',
                              password='pass')

        UsersService.add_user_to_database(expected_user)
        actual_user = list(Users.query.all())[0]

        self.assertEqual(actual_user, expected_user)

    # user_with_email_already_exists tests #
    def test_user_with_email_already_exists_already_exists(self):
        email = 'jake@jake.jake'
        user_1 = Users(email=email,
                       nickname='Jake Wilson',
                       password='pass')

        UsersService.add_user_to_database(user_1)

        self.assertTrue(UsersService.user_with_email_already_exists(email))

    def test_user_with_email_already_exists_does_not_exist(self):
        email = 'jake@jake.jake'
        self.assertFalse(UsersService.user_with_email_already_exists(email))

    def test_user_with_email_already_exists_capitalization_differences(self):
        email_1 = 'jake@jake.jake'
        email_2 = 'Jake@jake.jake'
        user_1 = Users(email=email_1,
                       nickname='Jake Wilson',
                       password='pass')

        UsersService.add_user_to_database(user_1)

        self.assertTrue(UsersService.user_with_email_already_exists(email_2))

    # get_list_of_all_users tests #
    def test_get_list_of_all_users_no_users(self):
        expected_list = []
        actual_list = UsersService.get_list_of_all_users()
        self.assertListEqual(actual_list, expected_list)

    def test_get_list_of_all_users_one_user(self):
        user_1 = Users(email='jake@jake.jake',
                       nickname='Jake Wilson',
                       password='pass')
        UsersService.add_user_to_database(user_1)
        expected_list = [user_1]
        actual_list = UsersService.get_list_of_all_users()

        self.assertListEqual(actual_list, expected_list)

    def test_get_list_of_all_users_three_users(self):
        user_1 = Users(email='jake@jake.jake',
                       nickname='Jake Wilson',
                       password='pass')
        user_2 = Users(email='brian@brian.brian',
                       nickname='Brian',
                       password='pass')
        user_3 = Users(email='jacob@jacob.jacob',
                       nickname='Jacob',
                       password='pass')

        UsersService.add_user_to_database(user_1)
        UsersService.add_user_to_database(user_2)
        UsersService.add_user_to_database(user_3)

        expected_results = [user_1, user_2, user_3]
        actual_results = UsersService.get_list_of_all_users()

        def sort_key(x):
            return x.email  # this is arbitrary

        # Service makes no guarantee of order of users returned
        self.assertListEqual(sorted(actual_results, key=sort_key), sorted(expected_results, key=sort_key))
