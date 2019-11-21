from unittest import TestCase
from unittest.mock import Mock, patch

from src.use_cases.list_users_use_case import ListUser


class TestCreateUserUseCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch("src.repositories.user_repo.UserRepo")
    def test_get_user_by_id(self, mock_user_repo):
        # mocking db dependency

        mock_user_repo.get.return_value = {'id': 1,
                                           'user_name': "badra",
                                           "password": "123456789"
                                           }

        create_user_uc = ListUser(repository=mock_user_repo)

        user = create_user_uc.execute(user_id=1)
        self.assertEqual(user,
                         [{'id': 1,
                           'user_name': "badra",
                           "password": "123456789"
                           }]
                         )

        mock_user_repo.get.assert_called_once_with(
            id=1
        )

    @patch("src.repositories.user_repo.UserRepo")
    def test_get_all_users(self, mock_user_repo):
        mock_user_repo.get_all.return_value = [{'id': 1,
                                           'user_name': "badra",
                                           "password": "123456789"
                                           },
                                           {'id': 2,
                                            'user_name': "badra1",
                                            "password": "1234567890"
                                            }
                                           ]

        create_user_uc = ListUser(repository=mock_user_repo)

        users = create_user_uc.execute(user_id=1)
        self.assertEqual(users,
                         [{'id': 1,
                           'user_name': "badra",
                           "password": "123456789"
                           },
                          {'id': 2,
                           'user_name': "badra1",
                           "password": "1234567890"
                           }
                          ]
                         )

        mock_user_repo.get_all.assert_count(1)
