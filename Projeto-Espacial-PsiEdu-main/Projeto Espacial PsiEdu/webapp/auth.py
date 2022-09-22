from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Profissional, Cliente
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login_profissional', methods=['GET', 'POST'])
def login_profissional():
    if request.method == 'POST':
        email_profissional = request.form.get('email_profissional')
        senha_profissional = request.form.get('senha_profissional')

        profissional = Profissional.query.filter_by(email_profissional=email_profissional).first()
        if profissional:
            if check_password_hash(profissional.senha_profissional, senha_profissional):
                flash('Logado com sucesso.', category='success')
                login_user(profissional, remember=True)
                return redirect(url_for('auth.portal_profissional'))
            else:
                flash('Senha incorreta, tente novamente.', category='error')
        else:
            flash('E-mail não existe.', category='error')

    return render_template("login_profissional.html", profissional=current_user)

@auth.route('/sair_profissional')
@login_required
def sair():
    logout_user()
    return redirect(url_for('auth.login_profissional'))

@auth.route('/cadastrar_profissional', methods=['GET', 'POST'])
def cadastrar_profissional():
    if request.method == 'POST':
        nome_profissional = request.form.get('nome_profissional')
        sobrenome_profissional = request.form.get('sobrenome_profissional')
        telefone_profissional = request.form.get('telefone_profissional')
        estado_profissional = request.form.get('estado_profissional')
        n_registro = request.form.get('n_registro')
        email_profissional = request.form.get('email_profissional')
        senha_profissional = request.form.get('senha_profissional')
        senha_profissionalConfirmar = request.form.get('senha_profissionalConfirmar')
        especialidade = request.form.get('especialidade')
        usuario_profissional = request.form.get('usuario_profissional')

        profissional_email =  Profissional.query.filter_by(email_profissional=email_profissional).first()
        profissional_usuario = Profissional.query.filter_by(usuario_profissional=usuario_profissional).first()
        if profissional_email:
            flash('E-mail já existe!', category='error')
        elif profissional_usuario:
            flash('Usuário já existe!', category='error')
        elif len(nome_profissional) < 1:
            flash('Insira um nome válido.', category='error')
        elif len(sobrenome_profissional) < 1:
            flash('Insira um sobrenome válido.', category='error')
        elif len(telefone_profissional) < 11:
            flash('Insira um telefone válido.', category='error')    
        elif estado_profissional not in "AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO EX":
            flash('Escolha seu estado.', category='error')       
        elif len(n_registro) < 1:
            flash('Insira um número de registro válido.', category='error')   
        elif len(email_profissional) < 1:
            flash('Insira um e-mail válido.', category='error')
        elif senha_profissional != senha_profissionalConfirmar:
            flash('Senha errada, tente novamente.', category='error')
        elif len(senha_profissional) < 1:
            flash('Insira uma senha válida.', category='error')
        elif especialidade not in "Psicológo Psicopedagógo Psiquiátra Psicanalista Professor Outros":
            flash('Escolha sua profissão.', category='error')                    
        else:
            novo_profissional = Profissional(
                nome_profissional=nome_profissional, 
                sobrenome_profissional=sobrenome_profissional, 
                telefone_profissional=telefone_profissional,
                estado_profissional=estado_profissional,
                n_registro=n_registro, 
                email_profissional=email_profissional, 
                usuario_profissional=usuario_profissional,
                senha_profissional=generate_password_hash(senha_profissional, method=('sha256')),
                especialidade=especialidade)

            db.session.add(novo_profissional)
            db.session.commit()
            login_user(novo_profissional, remember=True)
            flash('Conta cadastrada com sucesso.', category='success')
            return redirect(url_for('auth.login_profissional'))
    return render_template('cadastrar_profissional.html', profissional=current_user)


@auth.route('/editar_perfil_profissional/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_perfil_profissional(id):
    editar_profissional = Profissional.query.get_or_404(id)
    if request.method == "POST":
        editar_profissional.nome_profissional = request.form.get('nome_profissional')
        editar_profissional.sobrenome_profissional = request.form.get('sobrenome_profissional')
        editar_profissional.telefone_profissional = request.form.get('telefone_profissional')
        editar_profissional.estado_profissional = request.form.get('estado_profissional')
        editar_profissional.email_profissional = request.form['email_profissional']
        editar_profissional.usuario_profissional = request.form['usuario_profissional']
        try:
            db.session.commit()
            flash("Perfil editado com sucesso.")
            return render_template("editar_profissional.html", editar_profissional = editar_profissional, id=id)
        except:
            flash("Erro. Parece que houve um problema, tente novamente.")
            return render_template("editar_profissional.html", editar_profissional = editar_profissional, id=id)
    else:
        return render_template("editar_profissional.html", editar_profissional = editar_profissional, id=id)

@auth.route('/portal_profissional', methods=['GET', 'POST'])
@login_required
def portal_profissional():
    id = current_user.id
    editar_profissional = Profissional.query.get_or_404(id)
    if request.method == "POST":
        editar_profissional.nome_profissional = request.form.get('nome_profissional')
        editar_profissional.sobrenome_profissional = request.form.get('sobrenome_profissional')
        editar_profissional.telefone_profissional = request.form.get('telefone_profissional')
        editar_profissional.estado_profissional = request.form.get('estado_profissional')
        editar_profissional.email_profissional = request.form.get['email_profissional']
        editar_profissional.usuario_profissional = request.form.get['usuario_profissional']
        try:
            db.session.commit()
            flash("Perfil editado com sucesso.")
            return render_template("portal_profissional.html", editar_profissional = editar_profissional)
        except:
            flash("Erro. Parece que houve um problema, tente novamente.")
            return render_template("portal_profissional.html", editar_profissional = editar_profissional)
    else:
        return render_template("portal_profissional.html",  editar_profissional = editar_profissional, id=id)

    # return render_template('editar_profissional.html')

#Perfil Público (outras pessoas conseguem ver)
@auth.route('/<usuario_profissional>')
#@login_required
def perfil_profissional(usuario_profissional):
    perfil_profissional = Profissional.query.filter_by(usuario_profissional=usuario_profissional).first()
    return render_template("perfil_profissional.html", perfil_profissional=perfil_profissional)


@auth.route('/alterar_senha/<int:id>', methods=['GET', 'POST'])
@login_required
def alterar_senha_profissional(id):
    # id = current_user.id
    editar_profissional = Profissional.query.get_or_404(id)
    if request.method == "POST":
        editar_profissional.senha_profissional = generate_password_hash(request.form['senha_profissional'], method=('sha256'))
        editar_profissional.senha_profissionalConfirmar = request.form.get('senha_profissionalConfirmar')
        try:
            db.session.commit()
            flash("Perfil editado com sucesso.")
            return render_template("alterar_senha_profissional.html", editar_profissional = editar_profissional, id=id)
        except:
            flash("Erro. Parece que houve um problema, tente novamente.")
            return render_template("alterar_senha_profissional.html", editar_profissional = editar_profissional, id=id)
    else:
        return render_template("alterar_senha_profissional.html",  editar_profissional = editar_profissional, id=id)

@auth.route('/login_cliente', methods=['GET', 'POST'])
def login_cliente():
    if request.method == 'POST':
        email_cliente = request.form.get('email_cliente')
        senha_cliente = request.form.get('senha_cliente')

        cliente = Cliente.query.filter_by(email_cliente=email_cliente).first()
        if cliente:
            if check_password_hash(cliente.senha_cliente, senha_cliente):
                flash('Logado com sucesso.', category='success')
                login_user(cliente, remember=True)
                return redirect(url_for('auth.portal_cliente'))
            else:
                flash('Senha incorreta, tente novamente.', category='error')
        else:
            flash('E-mail não existe.', category='error')

    return render_template("login_cliente.html", cliente=current_user)



@auth.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome_cliente = request.form.get('nome_cliente')
        sobrenome_cliente = request.form.get('sobrenome_cliente')
        idade_cliente = request.form.get('idade_cliente')
        telefone_cliente = request.form.get('telefone_cliente')
        email_cliente = request.form.get('email_cliente')
        senha_cliente = request.form.get('senha_cliente')
        senha_clienteConfirmar = request.form.get('senha_clienteConfirmar')
        cliente_recomendado = request.form.get('cliente_recomendado')        
        tipo_atendimento = request.form.get('tipo_atendimento')
        descricao_cliente = request.form.get('descricao_cliente')

        cliente =  Cliente.query.filter_by(email_cliente=email_cliente).first()
        if cliente:
            flash('E-mail já existe!', category='error')
        elif len(nome_cliente) < 2:
            flash('Nome deve ter pelo menos 2 caracteres!', category='error')
        elif len(sobrenome_cliente) < 2:
            flash('Sobrenome deve ter pelo menos 2 caracteres!', category='error')
        # elif len(idade_cliente) < 2:
        #     flash('Data deve estar no formato correto!', category='error')
        elif len(telefone_cliente) < 9:
            flash('Telefone deve ter 9 numeros, não esqueça do DDD!', category='error')            
        elif len(email_cliente) < 4:
            flash('E-mail deve ter pelo menos 4 caracteres!', category='error')
        elif senha_cliente != senha_clienteConfirmar:
            flash('Senha errada, tente novamente!', category='error')
        elif len(senha_cliente) < 7:
            flash('Senha deve ter pelo menos 7 caracteres!', category='error')
        # elif recomendado_cliente not in "1 2 3 4 5":
        #     flash('Escolha uma opção!', category='error')                    
        # elif tipo_atendimento not in "1 2 3 4 5 6":
        #     flash('Escolha uma opção!', category='error')
        # elif len(descricao_cliente) < 1:
        #     flash('Campo não preenchido!', category='error')
        else:
            novo_cliente = Cliente(
                nome_cliente=nome_cliente, 
                sobrenome_cliente=sobrenome_cliente, 
                telefone_cliente=telefone_cliente, 
                idade_cliente=idade_cliente, 
                email_cliente=email_cliente, 
                senha_cliente=generate_password_hash(senha_cliente, method=('sha256')),
                cliente_recomendado=cliente_recomendado, 
                tipo_atendimento=tipo_atendimento, 
                descricao_cliente=descricao_cliente
                )
            db.session.add(novo_cliente)
            db.session.commit()
            login_user(novo_cliente, remember=True)
            flash('Conta cadastrada com sucesso!', category='success')
            return redirect(url_for('auth.login_cliente'))

    return render_template('cadastrar_cliente.html', user=current_user)

@auth.route('/portal_cliente', methods=['GET', 'POST'])
@login_required
def portal_cliente():
    id = current_user.id
    editar_cliente = Cliente.query.get_or_404(id)
    if request.method == "POST":
        editar_cliente.nome_cliente = request.form.get('nome_cliente')
        editar_cliente.sobrenome_cliente = request.form.get('sobrenome_cliente')
        editar_cliente.telefone_cliente = request.form.get('telefone_cliente')
        editar_cliente.email_cliente = request.form.get['email_cliente']
        try:
            db.session.commit()
            flash("Perfil editado com sucesso.")
            return render_template("portal_cliente.html", editar_cliente = editar_cliente)
        except:
            flash("Erro. Parece que houve um problema, tente novamente.")
            return render_template("portal_cliente.html", editar_cliente = editar_cliente)
    else:
        return render_template("portal_cliente.html",  editar_cliente = editar_cliente, id=id)

@auth.route('/editar_perfil_cliente/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_perfil_cliente(id):
    editar_cliente = Cliente.query.get_or_404(id)
    if request.method == "POST":
        editar_cliente.nome_cliente = request.form.get('nome_cliente')
        editar_cliente.sobrenome_cliente = request.form.get('sobrenome_cliente')
        editar_cliente.telefone_cliente = request.form.get('telefone_cliente')
        editar_cliente.idadeCliente = request.form.get('idadeCliente')
        editar_cliente.email_cliente = request.form.get('email_cliente')
        editar_cliente.cliente_recomendadoPagina = request.form.get('cliente_recomendadoPagina')
        editar_cliente.cliente_tipoAtendimento = request.form.get('cliente_tipoAtendimento')
        editar_cliente.descricao_cliente = request.form.get('descricao_cliente')
        try:
            db.session.commit()
            flash("Perfil editado com sucesso.")
            return render_template("editar_cliente.html", editar_cliente = editar_cliente, id=id)
        except:
            flash("Erro. Parece que houve um problema, tente novamente.")
            return render_template("editar_cliente.html", editar_cliente = editar_cliente, id=id)
    else:
        return render_template("editar_cliente.html", editar_cliente = editar_cliente, id=id)

@auth.route('/alterar_senha_cliente/<int:id>', methods=['GET', 'POST'])
@login_required
def alterar_senha_cliente(id):
    # id = current_user.id
    editar_cliente = Cliente.query.get_or_404(id)
    if request.method == "POST":
        editar_cliente.senha_cliente = generate_password_hash(request.form['senha_cliente'], method=('sha256'))
        editar_cliente.senha_clienteConfirmar = request.form.get('senha_clienteConfirmar')
        try:
            db.session.commit()
            flash("Perfil editado com sucesso.")
            return render_template("alterar_senha_cliente.html", editar_cliente = editar_cliente, id=id)
        except:
            flash("Erro. Parece que houve um problema, tente novamente.")
            return render_template("alterar_senha_cliente.html", editar_cliente = editar_cliente, id=id)
    else:
        return render_template("alterar_senha_cliente.html",  editar_cliente = editar_cliente, id=id)


@auth.route('/sair_cliente')
@login_required
def sair_cliente():
    logout_user()
    return redirect(url_for('auth.sair_cliente'))
