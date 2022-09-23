from . import db
from flask_login import UserMixin #módulo pra ajudar usuários a logar no aplicação.
from sqlalchemy.sql import func
from sqlalchemy.orm import backref

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)      # chave primaria
    nome_curso= db.Column(db.String(70))
    sobre_curso= db.Column(db.String(500))
    categoria_curso = db.Column(db.String(45))
    cronograma_curso = db.Column(db.String(70))
    preco_curso = db.Column(db.Numeric(10,0))
    carga_horaria = db.Column(db.String(45))
    possui_certificado = db.Column(db.String(45))
    conteudo_curso = db.Column(db.String(500))
    bibliografia_curso = db.Column(db.String(1000))
    metodo_pagamento = db.Column(db.String(70))
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissional.id'))     # chave estrangeira
    #foto_curso = db.Column(db.String(45))

class Profissional(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # chave primaria
    nome_profissional = db.Column(db.String(45))
    usuario_profissional = db.Column(db.String(30), unique=True)
    sobrenome_profissional = db.Column(db.String(45))
    telefone_profissional = db.Column(db.String(30))
    estado_profissional = db.Column(db.String(50))
    endereco_profissional = db.Column(db.String(150))
    n_registro = db.Column(db.String(30))
    email_profissional = db.Column(db.String(45), unique=True)
    senha_profissional = db.Column(db.String(150))  #150 caracteres pq vai aparecer criptografada no banco de dados
    especialidade = db.Column(db.String(30))
    foto_profissional = db.Column(db.String(1000), nullable=True) #Inserir uma foto do profissional no perfil depois.
    cursos = db.relationship('Curso', backref='responsavel', cascade='all, delete')  # um profissional para muitos cursos
    historico_profissional = db.relationship('Historico', backref='profissao', cascade='all, delete', uselist="False")  # um profissional para um historico

class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sobre_mim = db.Column(db.String(1500))
    idioma = db.Column(db.String(1500))

    nome_instituicao = db.Column(db.String(1500))
    curso_academico = db.Column(db.String(1500))
    data_inicio = db.Column(db.String(100))
    data_termino = db.Column(db.String(100))
    descricao_academica = db.Column(db.String(1500))


    experiencia_profissao = db.Column(db.String(1500))
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissional.id'), unique=True) 

class Cliente(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(45))
    sobrenome_cliente = db.Column(db.String(30), unique=True)
    telefone_cliente = db.Column(db.String(45))
    idade_cliente = db.Column(db.String(30))
    email_cliente = db.Column(db.String(45), unique=True)
    senha_cliente = db.Column(db.String(150))  #150 caracteres pq vai aparecer criptografada no banco de dados...
    cliente_recomendado = db.Column(db.String(50))
    tipo_atendimento = db.Column(db.String(30))
    descricao_cliente = db.Column(db.String(150))