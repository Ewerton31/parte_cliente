from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#Objeto do Banco de Dados
db = SQLAlchemy()
# DB_NOME = "db_psiedu.db"

def criar_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ProjetoEspacialPsiEduSecretKey'

    # Configuração do Banco de Dados

    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NOME}'  #Conector MYSQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/psiedu_db'  #Conector MYSQL
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import Profissional, Cliente

    # Gerenciar todos os logins da aplicação (Quem loga e quem desloga)
    gerenciar_login = LoginManager()
    gerenciar_login.login_message = u"Insira seus dados para acessar essa página."
    gerenciar_login.login_view = 'auth.login_profissional'
    gerenciar_login.init_app(app)

    @gerenciar_login.user_loader
    def carregar_login(id):
        return Profissional.query.get(int(id)) #Vai procurar pela chave primaria e comparar com os dados informados
    
    gerenciar_login_cliente = LoginManager()
    gerenciar_login_cliente.login_message = u"Insira seus dados para acessar essa página."
    gerenciar_login_cliente.login_view = 'auth.login_cliente'
    gerenciar_login_cliente.init_app(app)

    @gerenciar_login_cliente.user_loader
    def carregar_login_cliente(id):
        return Cliente.query.get(int(id))
    db.create_all(app=app)

    # criar_db(app)

    return app

# def criar_db(app):
#     if not path.exists('webapp/' + DB_NOME):
#         db.create_all(app=app)
#         print('Banco de dados criado!')