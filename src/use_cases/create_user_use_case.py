from entities.user import User

class CreateUserUseCase(object):
    def __init__(self, repository=None):
        # we inject the repository object as dependency to usecase
        self.db_repo = repository

    def execute(self, user_name, password):
        if user_name and password:
            user_entity = User(user_name=user_name, password=password)

            if not user_entity.validate_user_name():
                raise ValueError("Invalid user name")
            
            if not user_entity.validate_password():
                raise ValueError("Invalid password")

            # create user if data satisfies enterprise wide policy validations
            password = user_entity.get_encrypted_password()

            return self.db_repo.create(user_name=user_name, password=password)





