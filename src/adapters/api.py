#!flask/bin/python
from flask import Flask, jsonify
from flask import request

from repositories.user_repo import UserRepo

from use_cases import CreateUserUseCase
from use_cases import ListUser
from use_cases import LoginUserUseCase


app = Flask(__name__)

@app.route('/cleanapp/api/v1.0/user/<int:id>', methods=['GET'])
def get_user(id):
    user_repo = UserRepo()
    # injecting dependency to use case to interact with database
    list_user_uc = ListUser(repository=user_repo)
    user = list_user_uc.execute(user_id=id)

    # we can use serializers
    return jsonify({'user': user})


@app.route('/cleanapp/api/v1.0/user/', methods=['POST'])
def create_user():
    # here we can handle exceptions and give valid error messages to client
    if not request.json:
        abort(400)

    user_repo = UserRepo()
    create_user_uc = CreateUserUseCase(repository=user_repo)
    user = create_user_uc.execute(
        user_name=request.json['userName'],
        password=request.json['password']
    )

    return jsonify({'user': user}), 201

@app.route('/cleanapp/api/v1.0/users', methods=['GET'])
def get_users():
    user_repo = UserRepo()
    # injecting dependency to use case to interact with database
    list_user_uc = ListUser(repository=user_repo)
    users = list_user_uc.execute(user_id=None)

    return jsonify({'users': users})


@app.route('/cleanapp/api/v1.0/login/', methods=['POST'])
def login():
    if not request.json:
        abort(400)

    user_repo = UserRepo()
    login_uc = LoginUserUseCase(repository=user_repo)
    user = login_uc.execute(
        user_name=request.json['userName'],
        password=request.json['password']
    )
    if not user:
        return jsonify({'error': "Invalid username or password"})

    return jsonify({'user': user}), 200


if __name__ == '__main__':
    app.run(debug=True)