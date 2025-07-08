from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from database.db import db
from models.user_model import User

# Função para registrar um novo usuário
def register():
    data = request.json  # Recebe os dados JSON
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')  # Gera hash da senha
    new_user = User(username=data['username'], password=hashed_password)  # Cria novo usuário
    db.session.add(new_user)
    db.session.commit()  # Salva no banco
    return jsonify({'message': 'User criado com sucesso!'}), 201  # Retorna sucesso

# Função para login do usuário
def login():
    data = request.json  # Recebe os dados JSON
    user = User.query.filter_by(username=data['username']).first()  # Busca usuário pelo username
    if user and check_password_hash(user.password, data['password']):  # Verifica senha
        return jsonify({'message': 'Login com sucesso', 'user_id': user.id})  # Retorna sucesso
    return jsonify({'message': 'Credencial inválida'}), 401  # Retorna erro


# Função para obter um usuário pelo ID
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'Usuário não encontrado'}), 404
    return jsonify({ 'id': user.id, 'username': user.username })

# Função para atualizar um usuário
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'Usuário não encontrado'}), 404
    
    data = request.json
    user.username = data.get('username', user.username)
    if 'password' in data:
        user.password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    
    db.session.commit()
    return jsonify({'message': 'Usuário atualizado com sucesso'})

# Função para deletar um usuário
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'Usuário não encontrado'}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Usuário deletado com sucesso'})
