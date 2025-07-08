from database.db import db

# Modelo da tabela de formulários
class Formulario(db.Model):
    __tablename__ = 'formularios'  # Nome da tabela no banco

    id = db.Column(db.Integer, primary_key=True)  # ID único do formulário
    nome = db.Column(db.String(100), nullable=False)  # Nome da pessoa no formulário
    email = db.Column(db.String(120), nullable=False)  # E-mail informado no formulário
    data_nascimento = db.Column(db.Date, nullable=False)  # Data de nascimento como tipo Date
    cpf = db.Column(db.String(14), unique=True, nullable=False)  # CPF único
    genero = db.Column(db.String(20), nullable=False)  # Gênero
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # O relacionamento com User já está implícito pelo backref em 'user'
    # Não é necessário definir o relacionamento aqui, pois já é feito em 'User' (forms)

