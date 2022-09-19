from . import db
from flask_login import UserMixin #módulo pra ajudar usuários a logar no aplicação.
from sqlalchemy.sql import func


class Profissional(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome_profissional = db.Column(db.String(45))
    usuario_profissional = db.Column(db.String(30), unique=True)
    sobrenome_profissional = db.Column(db.String(45))
    telefone_profissional = db.Column(db.String(30))
    estado_profissional = db.Column(db.String(50))
    n_registro = db.Column(db.String(30))
    email_profissional = db.Column(db.String(45), unique=True)
    senha_profissional = db.Column(db.String(150))  #150 caracteres pq vai aparecer criptografada no banco de dados...
    especialidade = db.Column(db.String(30))
    #plano_assinatura  #Será revisado com uma API Stripe... pesquisar depois como integrar com a aplicação.
    #foto_profissional #Inserir uma foto do profissional no perfil depois.

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