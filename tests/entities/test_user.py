
from unittest import TestCase

from src.entities.user import User


class TestUser(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_validate_user_name_with_valid_data(self):

        user = User(user_name="testuser", password="Cleanapp@123")
        self.assertTrue(user.validate_user_name())

    def test_validate_user_name_with_invalid_data(self):

        user = User(user_name="testuser###", password="Cleanapp@123")
        self.assertRaises(ValueError, user.validate_user_name)

    def test_validate_password_policy_with_valid_password(self):

        user = User(user_name="badra123", password="Cleanapp@123")
        self.assertTrue(user.validate_password_policy())

    def test_validate_password_policy_with_invalid_password(self):

        user = User(user_name="badra123", password="Clean")
        self.assertFalse(user.validate_password_policy())

    def test_password_encryption(self):
        user = User(user_name="testuser", password="Cleanapp@123")
        # password is encrypted
        assert user.get_encrypted_password() != 'Cleanapp@123'




