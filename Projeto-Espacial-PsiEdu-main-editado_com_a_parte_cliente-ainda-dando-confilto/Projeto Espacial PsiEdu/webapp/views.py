from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . models import Profissional, Cliente, Curso, Historico

views = Blueprint('views', __name__)

# Rota para a página inicial da aplicação.
@views.route('/')
def inicio():
    return render_template('index.html', profissional=current_user)

# Rota para ler todos as tabelas adicionadas no banco de dados.
@views.route('/ver')
def ver_profissionais():
    return render_template('ver_tabelas.html', profissionais=Profissional.query.all(), cursos=Curso.query.all())

@views.errorhandler(404)
def page_404(e):
    return render_template('404.html'), 404

@views.errorhandler(500)
def page_500(e):
    return render_template('500.html'), 500

@views.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403
    




