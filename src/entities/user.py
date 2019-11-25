
class User(object):
    def __init__(self, user_name, password, **kwargs):
        self.user_name = user_name
        self.password = password

    def validate_user_name(self):
        # apply username validation as per your organization policy
        if not self.user_name:
            raise ValueError("user_name is required")

        if "#" in self.user_name:
            raise ValueError("Invalid username, please remove # from user name")

        return True

    def get_encrypted_password(self):
        if not self.password:
            raise ValueError("password is empty")

        if not self.validate_password_policy:
            raise ValueError("password is not meet with password requirments")

        # use some password encryption algorithm as per your organization standard
        # returning dummy encrypted password, 
        return "hkhdde9ldajaldjqemamc"

    def validate_password_policy(self):
        # we can apply all password rules here
        if len(self.password) <= 8:
            return False

        return True
