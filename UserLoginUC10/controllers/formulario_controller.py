from flask import request, jsonify
from database.db import db
from models.formulario_model import Formulario
from datetime import datetime  # Importando datetime para a conversão da data

# Função para criar um novo formulário
def create_form():
    data = request.json  # Recebe os dados JSON
    # Converte a data de nascimento para objeto date
    data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()

    new_form = Formulario(
        nome=data['nome'],
        email=data['email'],
        data_nascimento=data_nascimento,  # Usando a data convertida
        cpf=data['cpf'],
        genero=data['genero'],
        user_id=data['user_id']  # Associa formulário a um usuário
    )
    db.session.add(new_form)
    db.session.commit()  # Salva no banco
    return jsonify({'message': 'Form cadastrado com sucesso!'}), 201  # Retorna sucesso

# Função para obter todos os formulários
def get_forms():
    forms = Formulario.query.all()  # Busca todos os formulários
    return jsonify([{  # Retorna lista de formulários
        'id': form.id,
        'nome': form.nome,
        'email': form.email,
        'data_nascimento': form.data_nascimento,
        'cpf': form.cpf,
        'genero': form.genero,
        'user_id': form.user_id
    } for form in forms])

# Função para obter um formulário pelo ID
def get_form_by_id(form_id):
    form = Formulario.query.get(form_id)
    if not form:
        return jsonify({'message': 'Formulário não encontrado'}), 404
    return jsonify({
        'id': form.id,
        'nome': form.nome,
        'email': form.email,
        'data_nascimento': form.data_nascimento,
        'cpf': form.cpf,
        'genero': form.genero,
        'user_id': form.user_id
    })

# Função para atualizar um formulário
def update_form(form_id):
    form = Formulario.query.get(form_id)
    if not form:
        return jsonify({'message': 'Formulário não encontrado'}), 404
    
    data = request.json

    # Converte a nova data se fornecida
    if 'data_nascimento' in data:
        form.data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
    else:
        form.data_nascimento = data.get('data_nascimento', form.data_nascimento)
    
    form.nome = data.get('nome', form.nome)
    form.email = data.get('email', form.email)
    form.cpf = data.get('cpf', form.cpf)
    form.genero = data.get('genero', form.genero)
    form.user_id = data.get('user_id', form.user_id)
    
    db.session.commit()
    return jsonify({'message': 'Formulário atualizado com sucesso'})

# Função para deletar um formulário
def delete_form(form_id):
    form = Formulario.query.get(form_id)
    if not form:
        return jsonify({'message': 'Formulário não encontrado'}), 404
    
    db.session.delete(form)
    db.session.commit()
    return jsonify({'message': 'Formulário deletado com sucesso'})

