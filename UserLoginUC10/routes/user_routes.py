from flask import Blueprint
from controllers.user_controller import (
    register, login, get_user_by_id, update_user, delete_user
)

# Blueprint para as rotas de usuário
user_bp = Blueprint('users', __name__)

# Rota para cadastro de usuário
@user_bp.route('/register', methods=['POST'])
def register_user():
    return register()

# Rota para login de usuário
@user_bp.route('/login', methods=['POST'])
def login_user():
    return login()


# Rota para obter um usuário pelo ID
@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return get_user_by_id(user_id)

# Rota para atualizar um usuário
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user_info(user_id):
    return update_user(user_id)

# Rota para deletar um usuário
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_info(user_id):
    return delete_user(user_id)


