
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

        # use some password encryption algorithm as per your organization standard
        # returning dummy encrypted password, 
        return "hkhdde9ldajaldjqemamc"

        
