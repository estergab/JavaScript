from database.db import db

# Modelo da tabela de usuários
class User(db.Model):
    __tablename__ = 'users'  # Nome da tabela no banco

    id = db.Column(db.Integer, primary_key=True)  # ID único do usuário
    username = db.Column(db.String(100), unique=True, nullable=False)  # Nome de usuário único
    password = db.Column(db.String(200), nullable=False)  # Senha hash do usuário

    # Relacionamento com formulários
    forms = db.relationship('Formulario', backref=db.backref('user', lazy=True), cascade='all, delete-orphan')
