
class ListUser(object):

    def __init__(self, repository=None):
        self.db_repo = repository

    def execute(self, user_id):
        users = []
        if user_id:
            users.append(self.db_repo.get(user_id=user_id))
        else:
            users = self.db_repo.get_all()

        # adapter serialize this data as per their requirments(ex: json, xml, render as html pages)
        return users

