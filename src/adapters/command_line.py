import argparse

from repositories.user_repo import UserRepo

from use_cases import CreateUserUseCase
from use_cases import ListUser
from use_cases import LoginUserUseCase

ACTIONS = ["login", 'create_user']


def create_user(user_name, password):

    user_repo = UserRepo()
    create_user_uc = CreateUserUseCase(repository=user_repo)
    user = create_user_uc.execute(
        user_name=user_name,
        password=password
    )
    return "user created successfully, user id is {}".format(user.id)


def login(user_name, password):

    user_repo = UserRepo()
    login_uc = LoginUserUseCase(repository=user_repo)
    user = login_uc.execute(
        user_name=user_name,
        password=password
    )

    if not user:
        return "Invalid user name or password"

    return "success"




def main():
    # create parser object
    parser = argparse.ArgumentParser(description="A clean app interface")

    # defining arguments for parser object
    parser.add_argument("-u", "--user_name",
                        type=str,
                        help="Enter user name")

    parser.add_argument("-p", "--password",
                        type=str,
                        help="Enter password")

    parser.add_argument("-a", "--action",
                        type=str,
                        help="example: login or create_user")

    # parse the arguments from standard input
    args = parser.parse_args()

    if not args.action:
        return "please provide --action info"

    if args.action not in ACTIONS:
        return "Invalid Action name (--action)"

    if args.action == 'login':
        return login(user_name=args.user_name, password=args.password)

    elif args.action == 'create_user':
        return create_user(user_name=args.user_name, password=args.password)



"""
usage note:

$ python command_line.py --user_name "badra"  --password "cleanapp@1234" --action "login"

$ python command_line.py --user_name "badra"  --password "cleanapp@1234" --action "create_user"


"""


if __name__ == "__main__":
    main()

