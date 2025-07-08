
from flask import Flask
from database.db import db
from config import Config
from routes.user_routes import user_bp
from routes.formulario_routes import formulario_bp

# Inicializa a aplicação Flask
app = Flask(__name__)
app.config.from_object(Config)  # Configurações da aplicação

db.init_app(app)  # Inicializa o banco de dados com a aplicação

# Registra as rotas dos usuários e formulários
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(formulario_bp, url_prefix='/forms')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados se não existirem
    app.run(debug=True)  # Inicia o servidor Flask