

class LoginUserUseCase(object):

    def __init__(self, repository=None):
        # we inject the repository object as dependency to usecase
        self.db_repo = repository

    def execute(self, user_name, password):
        if user_name and password:
            if self.db_repo.validate_user(user_name=user_name, password=password):
                return True
            else:
                raise ValueError("Invalid user name and password")
