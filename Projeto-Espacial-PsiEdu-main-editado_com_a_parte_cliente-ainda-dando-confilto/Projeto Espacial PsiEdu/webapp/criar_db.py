#Esse arquivo só roda uma vez pra criar o banco de dados, por isso eu comentei o comando abaixo de create database.
#Use esse arquivo somente se precisar criar o banco de dados pro localhost.
import mysql.connector 


#Conexão com o banco de dados
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='sua_senha_do_mysql',
)

#Objeto para comandos
c = db.cursor()


#Comando para CRIAR o banco de dados

#c.execute('CREATE DATABASE psiedu_db')


#Comando para mostra todos os bancos de dados criados na sua máquina.
c.execute('SHOW DATABASES')
for i in c:
    print(i)