from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#Objeto do Banco de Dados
db = SQLAlchemy()
# DB_NOME = "db_psiedu.db"

def criar_app():
    
    # Configuração do aplicativo Flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ProjetoEspacialPsiEduSecretKey'
    app.config['TRAP_HTTP_EXCEPTIONS']=True
    # Configuração para salvar as imagens carregas na aplicação
    CARREGAR_PASTA = 'static/assets/img/foto_perfil/'
    app.config['CARREGAR_PASTA'] = CARREGAR_PASTA

    # Configuração do Banco de Dados

    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NOME}'  #Conector MYSQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/psiedu_db'  #Conector MYSQL
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    @app.errorhandler(404)
    def page_404(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def page_500(e):
        return render_template('500.html'), 500

    @app.errorhandler(403)
    def page_not_found(e):
        return render_template('403.html'), 403
    
    from .models import Profissional, Cliente, Curso, Historico

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
