from asyncio.windows_events import NULL
from msilib.schema import Error
import mysql.connector

from datetime import datetime
import sys
sys.path.insert(1,'D:\OneDrive\Aztec Energia Compartilhada (1)\TIME\João Luiz\Projeto API - Monitoramentos -m Jaguar.login')

def conect():

    global conn 

    global cursor

    while True:

        try:
            mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "@Zt3cenergia"
            )
            cursor = conn.cursor()
            conn.commit()

        except:
            
            cursor = conn.cursor()

            criando_bd = """ CREATE DATABASE Usuarios; """
                                                    
            cursor.execute(criando_bd)

            conn.commit()
        
    #Cria e define a variável 'cursor' como global, já que todas as funções deste
    #módulo usam essa variável

    
    #Define a variável 'cursor' como  uma variável que irá intermediar a comunicação
    #definindo-a como um tipo cursor por meio da função 'cursor()'

def user(login,senha):

    conect()

    #Chamada da função 'conect()', que serve para realizar a conexão de cada função com
    #o servidor. Este trecho foi definido como função já que ele se repetia em todas as
    #funções

    print("Verificando se a tabela existe...")
    
    ver_logacessos = ('''SELECT * FROM INFORMATION_SCHEMA.TABLES
                         WHERE TABLE_SCHEMA = 'TheSchema'
                         AND TABLE_NAME = 'Log_Acessos' ''')

    #Verifica se o Banco de Dados 'Log_Acessos' existe

    cursor.execute(ver_logacessos)
    #Executa o comando SQL, inserido na variável 'ver_logacessos'

    conn.commit()

    if ver_logacessos == []:
    #Condicional que verifica se a variável 'ver_logacessos' tem algum valor
    #Se a variável estiver vazia executa o trecho abaixo
        
        try:
            criando_tabel = """CREATE TABLE Log_Acessos (
                                       nome VARCHAR(40),
                                       senha VARCHAR(40));"""
            #'criando_bd' recebe o comando SQL para criação do banco de dados

            cursor.execute(criando_tabel)
            #Executa o comando criado acima

            conn.commit()

        except:
            print("Erro ao criar tabela!")
    
    else:
    #Se a variável 'ver_logacessos' não estiver vazia, haverá a verificação de se
    #o banco de dados está vazio

        SQLCommand = ("INSERT INTO Log_Acessos(nome, senha) VALUES (?,?);")
        Values = (login, senha)

        cursor.execute(SQLCommand,Values)

        conn.commit()
    
    #Confirma as alterações realizadas pelo usuário

    print("Login Criado com Sucesso!")
    
    conn.close()
    #Termina a comunicação com o servidor 

def consulta_user():

    log = input("Insira seu login: ")
    pas = input("Insira sua senha: ")

    conect()

    cursor.execute('SELECT * FROM Log_Acessos')

    for row in cursor:
        
        usuario = row[0]
        passw = row[1]
            
        lastchar = len(passw)
        passw = passw[0:lastchar]
            
        if usuario==log and passw==pas:
            print("Olá,", usuario)
            return True
            
        else:
            print("Dados incorretos, tente novamente!")
            Login()

def pop(id_locais, nome_cliente, energia_dia):
         
    conect()

    SQLCommand = """SELECT count(*) as tot FROM Dados"""
    cursor.execute(SQLCommand)
    data = cursor.fetchone()
    conn.commit()
    
    if(data == NULL):

        conect()

        SQLCommand = (" INSERT INTO Dados(cliente_id, nome, ger_prim, date_prim, ger_seg, date_seg) VALUES (?,?,?,?,?,?); ")
                                        
        Values = (id_locais, nome_cliente, energia_dia, datetime.now(),NULL, NULL)

        cursor.execute(SQLCommand,Values)

        conn.commit()

        conn.close()
        
        #pop_seg(id_locais,energia_dia)

        return True

    else:

        conect()

        SQLCommand = ('''UPDATE Dados
                         SET ger_prim = (?), date_prim = (?)
                         WHERE cliente_id = (?);''')
                                        
        Values = (energia_dia, datetime.now(),id_locais)
    
        cursor.execute(SQLCommand,Values)

        conn.commit()

        conn.close()

        #pop_seg(id_locais,energia_dia)

        return True

def consulta_pop():

    conect()

    info = cursor.execute('SELECT * FROM Dados').fetchall()

    dados_relat = []

    for x in range(len(info)):
        dados_relat.append(info[x])

    return dados_relat

def pop_seg(id_locais, energia_dia):
        
    conect()

    SQLCommand = ('''UPDATE Dados
                     SET ger_seg = (?), date_seg = (?)
                     WHERE cliente_id = (?);''')
                                       
    Values = (energia_dia, datetime.now(),id_locais)
  
    cursor.execute(SQLCommand,Values)

    conn.commit()

    conn.close()

           
                   