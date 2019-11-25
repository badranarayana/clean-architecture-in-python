"""
Define repos to abstract orm models and queries

"""
from src.models.user_model import User  

class UserRepo(object):
     """
     This class is to write all user specific queries
     """

    def get(id):
        # use the ORM models to query the database
        return User.objects.filter(id=id)

    def create(user_name, password, **kwargs):
        user = User(user_name=user_name, password=password)
        user.save()

    def get_all():
        return User.objects.all()

    def get_active_users():
        # write a query to get only active users
        pass

    def get_password_expired_users():
        pass

    def is_user_name_exits():
        # write a query to check the user name existence in db
        pass

    def validate_user(user_name, password):
        pass
