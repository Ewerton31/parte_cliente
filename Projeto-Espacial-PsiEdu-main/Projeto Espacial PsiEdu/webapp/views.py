from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . models import Profissional

views = Blueprint('views', __name__)

# Rota para a página inicial da aplicação.
@views.route('/')
#@login_required
def inicio():
    return render_template('index.html', profissional=current_user)

# Rota para ler todos os profissionais adicionados no banco de dados.
@views.route('/ver')
#@login_required
def ver_profissionais():
    return render_template('ver_profissionais.html', profissionais=Profissional.query.all())