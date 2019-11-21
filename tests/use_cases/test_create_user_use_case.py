
from unittest import TestCase
from unittest.mock import Mock, patch

from src.use_cases.create_user_use_case import CreateUserUseCase
from src.entities.user import User


class TestCreateUserUseCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch("src.repositories.user_repo.UserRepo")
    def test_create_user_valid_data(self, mock_user_repo):

        mock_user_repo.create.return_value = Mock()

        create_user_uc = CreateUserUseCase(repository=mock_user_repo)

        create_user_uc.execute(user_name="badra", password="Clean@12347")

        encrypted_password = User(user_name="badra", password="Clean@12347").get_encrypted_password()

        mock_user_repo.create.assert_called_once_with(
            user_name="badra",
            password=encrypted_password
        )

    @patch("src.repositories.user_repo.UserRepo")
    def test_create_user_empty_data(self, mock_user_repo):
        mock_user_repo.create.return_value = Mock()

        create_user_uc = CreateUserUseCase(repository=mock_user_repo)

        self.assertRaises(ValueError, create_user_uc.execute, user_name="", password="")
