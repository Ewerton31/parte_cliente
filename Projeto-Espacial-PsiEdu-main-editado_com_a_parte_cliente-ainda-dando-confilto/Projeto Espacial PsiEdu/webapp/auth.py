from sqlite3 import IntegrityError
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from .models import Profissional, Cliente, Curso, Historico
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename
import uuid as uuid
import os

auth = Blueprint('auth', __name__)


@auth.errorhandler(404)
def page_404(e):
    return render_template("404.html"), 404

@auth.errorhandler(500)
def page_500(e):
    return render_template("500.html"), 500

@auth.errorhandler(403)
def page_not_found(e):
    return render_template("403.html"), 403
    

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
        endereco_profissional = request.form.get('endereco_profissional')
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
                endereco_profissional=endereco_profissional,
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
        editar_profissional.endereco_profissional = request.form.get('endereco_profissional')
        editar_profissional.email_profissional = request.form.get('email_profissional')
        editar_profissional.usuario_profissional = request.form.get('usuario_profissional')
        if request.files.get('foto_profissional'): # Se o request for só a foto
            editar_profissional.foto_profissional = request.files.get('foto_profissional')
            foto_arquivo_nome = secure_filename(editar_profissional.foto_profissional.filename)
            #Montar o UUID
            foto_nome = str(uuid.uuid1()) + "_" + foto_arquivo_nome
            #Salvar imagem
            salvar = request.files.get('foto_profissional')
            basedir = os.path.abspath(os.path.dirname(__file__)) #código para corrigir o erro de diretorio
            editar_profissional.foto_profissional = foto_nome
            try:
                db.session.commit()
                salvar.save(os.path.join(basedir, current_app.config['CARREGAR_PASTA'], foto_nome))
                flash("Foto alterada com sucesso.", category='success')
                return render_template("editar_profissional.html", editar_profissional = editar_profissional, id=id)
            except IntegrityError:
                db.session.rollback()
                flash("Usuário/E-mail já existe, tente novamente.", category='error')
                return render_template("editar_profissional.html", editar_profissional = editar_profissional, id=id)
        else:
            db.session.add(editar_profissional)
            db.session.commit()
            flash("Perfil editado com sucesso.", category='success')
            return render_template("editar_profissional.html", editar_profissional = editar_profissional, id=id) 
    else:
        return render_template("editar_profissional.html", editar_profissional = editar_profissional, id=id)

@auth.route('/portal_profissional', methods=['GET', 'POST'])
@login_required
def portal_profissional():
    return render_template("portal_profissional.html")


@auth.route('/alterar_senha/<int:id>', methods=['GET', 'POST'])
@login_required
def alterar_senha_profissional(id):
    editar_profissional = Profissional.query.get_or_404(id)
    if request.method == "POST":
        editar_profissional.senha_profissional = request.form.get('senha_profissional')
        editar_profissional.senha_profissionalConfirmar = request.form.get('senha_profissionalConfirmar')
        if editar_profissional.senha_profissional != editar_profissional.senha_profissionalConfirmar:
            flash('Senha incorreta, tente novamente.', category='error')
            return render_template("alterar_senha_profissional.html", editar_profissional=editar_profissional, id=id)
        else:
            editar_profissional.senha_profissional = generate_password_hash(request.form.get('senha_profissional'), method=('sha256'))
            db.session.commit()
            flash("Perfil editado com sucesso.")
            return render_template("alterar_senha_profissional.html", editar_profissional=editar_profissional, id=id)
    else:
        return render_template("alterar_senha_profissional.html",  editar_profissional=editar_profissional, id=id)



@auth.route('/adicionar_cursos', methods=['GET', 'POST'])
@login_required
def adicionar_cursos():
    if request.method == 'POST':
        responsavel = current_user.id
        nome_curso = request.form.get('nome_curso')
        sobre_curso = request.form.get('sobre_curso')
        categoria_curso = request.form.get('categoria_curso')
        carga_horaria = request.form.get('carga_horaria')
        possui_certificado = request.form.get('possui_certificado')
        conteudo_curso = request.form.get('conteudo_curso')
        cronograma_curso = request.form.get('cronograma_curso')
        bibliografia_curso = request.form.get('bibliografia_curso')
        preco_curso  = request.form.get('preco_curso')
        metodo_pagamento = request.form.get('metodo_pagamento')
        if len(nome_curso) < 1:
            flash('Muito curto', category='error')
        elif categoria_curso == "Aula" and possui_certificado == "Sim":
            flash('Erro. Apenas cursos podem possuir certificados.', category='error')
        else:
            novo_curso = Curso(
                profissional_id = responsavel,
                nome_curso=nome_curso, 
                sobre_curso=sobre_curso, 
                categoria_curso=categoria_curso,
                carga_horaria=carga_horaria, 
                possui_certificado=possui_certificado, 
                conteudo_curso=conteudo_curso, 
                cronograma_curso=cronograma_curso,
                bibliografia_curso=bibliografia_curso,
                preco_curso=preco_curso,
                metodo_pagamento=metodo_pagamento
                )
            db.session.add(novo_curso)
            db.session.commit()
            flash('Curso adicionado com sucesso.', category='success')
    return render_template("adicionar_cursos.html")

@auth.route('/cursos')
def cursos():
	cursos = Curso.query.all()
	return render_template("cursos_profissional.html", cursos=cursos)

@auth.route('/meus_servicos')
def meus_servicos():
	cursos = Curso.query.all()
	return render_template("meus_servicos.html", cursos=cursos)

@auth.route('/cursos/<int:id>')
def curso(id):
	curso = Curso.query.get_or_404(id)
	return render_template('mostrar_cursos.html', curso=curso)
    
@auth.route('/cursos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_cursos(id):
    curso = Curso.query.get_or_404(id)
    if request.method == 'POST':
        curso.nome_curso = request.form.get('nome_curso')
        curso.sobre_curso = request.form.get('sobre_curso')
        curso.categoria_curso = request.form.get('categoria_curso')
        curso.carga_horaria = request.form.get('carga_horaria')
        curso.possui_certificado = request.form.get('possui_certificado')
        curso.conteudo_curso = request.form.get('conteudo_curso')
        curso.cronograma_curso = request.form.get('cronograma_curso')
        curso.bibliografia_curso = request.form.get('bibliografia_curso')
        curso.preco_curso  = request.form.get('preco_curso')
        curso.metodo_pagamento = request.form.get('metodo_pagamento')
        try:
            db.session.add(curso)
            db.session.commit()
            flash("Curso foi editado com sucesso", category='success')
            return render_template("editar_cursos.html", curso=curso)
        except:
            flash("Erro. Parece que houve um problema, tente novamente.", category="error")
            return render_template("editar_cursos.html", curso=curso)
    if current_user.id == curso.profissional_id:
        return render_template("editar_cursos.html", curso=curso)
    else:
        flash("Você não tem permissão para editar esse curso/aula.", category='error')
        cursos = Curso.query.all()
        return render_template("cursos_profissional.html", cursos=cursos)         

@auth.route('/cursos/deletar/<int:id>', methods=['GET', 'POST'])
@login_required
def deletar_cursos(id):
    deletar_cursos = Curso.query.get_or_404(id)
    id = current_user.id
    if id == deletar_cursos.responsavel.id:
        try:
            db.session.delete(deletar_cursos)
            db.session.commit()
            flash("Curso deletado com sucesso!", category='success')
            cursos = Curso.query.all()
            return render_template("meus_servicos.html", cursos=cursos)
        except:
            flash("Erro. Parece que houve um problema, tente novamente.", category="error")
            cursos = Curso.query.all()
            return render_template("meus_servicos.html", cursos=cursos)
    else:
        flash("Você não tem permissão para deletar esse curso/aula.", category='error')
        cursos = Curso.query.all()
        return render_template("cursos_profissional.html", cursos=cursos) 

@auth.route('/buscar', methods=['POST'])
def buscar():
    cursos = Curso.query
    if request.method == 'POST':
        buscado = request.form.get('buscado')
        cursos = cursos.filter(Curso.conteudo_curso.like('%' + buscado + '%'))
        cursos = cursos.order_by(Curso.nome_curso).all()
        return render_template("buscar.html", buscado=buscado, cursos=cursos)


@auth.route('/deletar/<int:id>', methods=['GET', 'POST'])
@login_required
def deletar_profissional(id):
    deletar_profissional = Profissional.query.get_or_404(id)
    if id == current_user.id:
        try:
            db.session.delete(deletar_profissional)
            db.session.commit()
            flash("Conta deletada com sucesso!", category='success')
            profissionais = Profissional.query.all()
            return render_template("login_profissional.html", profissionais=profissionais)
        except:
            flash("Erro. Parece que houve um problema, tente novamente.", category="error")
            profissionais = Profissional.query.all()
            return render_template("login_profissional.html", profissionais=profissionais)
    else:
        flash("Você não tem permissão para deletar este usuário.", category='error')
        profissionais = Profissional.query.all()
        return render_template("portal_profissional.html", profissionais=profissionais) 


#Perfil Público (outras pessoas conseguem ver)
@auth.route('/<usuario_profissional>')
#
def perfil_profissional(usuario_profissional):
    perfil_profissional = Profissional.query.filter_by(usuario_profissional=usuario_profissional).first()
    historico = Historico.query.all()
    return render_template("perfil_profissional.html", perfil_profissional=perfil_profissional, historico=historico)


@auth.route('/adicionar_historico_profissional', methods=['GET', 'POST'])
@login_required
def adicionar_historico_profissional():
    if request.method == 'POST':
        profissao = current_user.id
        sobre_mim = request.form.get('sobre_mim')
        idioma = request.form.get('idioma')
        nome_instituicao = request.form.get('nome_instituicao')
        curso_academico = request.form.get('curso_academico')
        data_inicio = request.form.get('data_inicio')
        data_termino = request.form.get('data_termino')
        descricao_academica = request.form.get('descricao_academica')
        experiencia_profissao = request.form.get('experiencia_profissao')

        if len(sobre_mim) < 1:
            flash('Muito curto', category='error')
        else:
            try:
                novo_perfil = Historico(
                    profissional_id = profissao,
                    sobre_mim = sobre_mim,
                    idioma = idioma,
                    nome_instituicao = nome_instituicao,
                    curso_academico = curso_academico,
                    data_inicio = data_inicio,
                    data_termino = data_termino,
                    descricao_academica = descricao_academica,
                    experiencia_profissao = experiencia_profissao
                    )
                db.session.add(novo_perfil)
                db.session.commit()
                flash('Histórico profissional adicionado com sucesso.', category='success')
            except IntegrityError:
                db.session.rollback()
                flash("Você já criou um histórico profissional no nosso sistema, você pode acessar a página de editar no seu perfil.", category='error')
    return render_template("adicionar_historico_profissional.html")


@auth.route('/editar_historico_profissional/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_historico_profissional(id):
    historico = Historico.query.get_or_404(id)
    if request.method == 'POST':
        historico.sobre_mim = request.form.get('sobre_mim')
        historico.experiencia_profissao = request.form.get('experiencia_profissao')
        historico.formacao_academica = request.form.get('formacao_academica')
        try:
            db.session.add(historico)
            db.session.commit()
            flash("Histórico profissional foi editado com sucesso.", category='success')
            return render_template("editar_historico_profissional.html", historico=historico)
        except:
            flash("Erro. Parece que houve um problema, tente novamente.", category="error")
            return render_template("editar_historico_profissional.html", historico=historico)
    if current_user.id == historico.profissional_id:
        return render_template("editar_historico_profissional.html", historico=historico)
    else:
        flash("Você não tem permissão para editar esse histórico profissional.", category='error')
        historico = Historico.query.all()
        return render_template("portal_profissional.html", historico=historico)

#Rotas de Cliente
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