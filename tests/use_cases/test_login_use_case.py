from unittest import TestCase
from unittest.mock import Mock, patch

from src.use_cases.login_use_case import LoginUserUseCase

from src.entities.user import User


class TestLoginUseCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch("src.repositories.user_repo.UserRepo")
    def test_login_user_with_valid_credentials(self, mock_user_repo):

        mock_user_repo.validate_user.return_value = True

        login_uc = LoginUserUseCase(repository=mock_user_repo)

        is_valid_user = login_uc.execute(user_name='badra', password="123456789")

        self.assertTrue(is_valid_user)

        encrypted_password = User(user_name="badra", password="123456789").get_encrypted_password()

        mock_user_repo.validate_user.assert_called_once_with(user_name='badra',
                                                             password=encrypted_password
                                                             )

    @patch("src.repositories.user_repo.UserRepo")
    def test_login_user_with_invalid_credentials(self, mock_user_repo):

        mock_user_repo.validate_user.return_value = False

        login_uc = LoginUserUseCase(repository=mock_user_repo)

        is_valid_user = login_uc.execute(user_name='badra',
                                         password="123456789")

        self.assertFalse(is_valid_user)

        encrypted_password = User(user_name="badra",
                                  password="123456789").get_encrypted_password()

        mock_user_repo.validate_user.assert_called_once_with(user_name='badra',
                                                             password=encrypted_password
                                                             )

    @patch("src.repositories.user_repo.UserRepo")
    def test_login_user_with_empty_credentials(self, mock_user_repo):
        mock_user_repo.validate_user.return_value = False

        login_uc = LoginUserUseCase(repository=mock_user_repo)

        self.assertRaises(ValueError, login_uc.execute, user_name='', password='')
