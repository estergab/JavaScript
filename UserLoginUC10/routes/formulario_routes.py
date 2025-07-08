from flask import Blueprint
from controllers.formulario_controller import (
    create_form, get_forms, get_form_by_id, update_form, delete_form
)

# Blueprint para as rotas de formulários
formulario_bp = Blueprint('forms', __name__)

# Rota para criar um formulário
@formulario_bp.route('/', methods=['POST'])
def create_new_form():
    return create_form()

# Rota para listar todos os formulários
@formulario_bp.route('/', methods=['GET'])
def list_forms():
    return get_forms()

# Rota para obter um formulário pelo ID
@formulario_bp.route('/<int:form_id>', methods=['GET'])
def get_single_form(form_id):
    return get_form_by_id(form_id)

# Rota para atualizar um formulário
@formulario_bp.route('/<int:form_id>', methods=['PUT'])
def update_existing_form(form_id):
    return update_form(form_id)

# Rota para deletar um formulário
@formulario_bp.route('/<int:form_id>', methods=['DELETE'])
def delete_existing_form(form_id):
    return delete_form(form_id)

