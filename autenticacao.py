import integracao_sql as sql
import pyodbc as dbc
from hashlib import sha256

def autenticar(login, senha):
    cursor, conexao = sql.juncao_sql()
    
    cursor.execute("select login from administrador")
    adm_logins = [row[0] for row in cursor.fetchall()]
        
    cursor.execute("select nome from usuario")
    usuario_logins = [row[0] for row in cursor.fetchall()]
    
    cursor.execute(f"select senha from administrador where login = ?",(login))
    adm_senha = [row[0] for row in cursor.fetchall()]
    
    cursor.execute(f"select id from usuario where nome = ?",(login))
    usuario_senha = [row[0] for row in cursor.fetchall()]
        
    if login in adm_logins:
        
        #senha_criptografada = sha256(senha.encode()).hexdigest()
        senha_criptografada = senha

        if senha_criptografada in adm_senha:
            print("Bem-vindo ADM")
            return True

        else:
            print("Senha incorreta tente novamente")
            return False
        
    elif login in usuario_logins:
        if senha in usuario_senha: 
            print("Bem-vindo usuário")
            return True

        else:
            print("ID errado tente novamente")
            return False
        
    else:      
        print("Login inválido tente novamente")
        return False

'''
import integracao_sql as sql
import pyodbc as dbc
from hashlib import sha256

def autenticar(login, senha):
    cursor, conexao = sql.juncao_sql()
    
    if not cursor or not conexao:
        return False
    
    try:
        query = 'SELECT * FROM administrador WHERE login = ? AND senha = ?'
        cursor.execute(query, (login, senha))
        
        resultado = cursor.fetchone()
        
        if resultado:
            print("Login efetuado com sucesso")
            return True
        else:
            print("Login ou senha incorretos")
            return False
    except dbc.Error as e:
        print(f"Erro ao consultar o banco de dados: {e}")
        return False
'''

'''
import integracao_sql
import pandas as pd
from hashlib import sha256

integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def autentificacao(): 
    
    login = input(f"Digite seu login se for ADM o digite seu nome se for usuário: ")
    
    cursor.execute("select login from administrador")
    adm_logins = [row[0] for row in cursor.fetchall()]
        
    cursor.execute("select nome from usuario")
    usuario_logins = [row[0] for row in cursor.fetchall()]
    
    cursor.execute(f"select senha from administrador where login = ?",(login))
    adm_senha = [row[0] for row in cursor.fetchall()]
    
    cursor.execute(f"select id from usuario where nome = ?",(login))
    usuario_senha = [row[0] for row in cursor.fetchall()]
        
    if login in adm_logins:
        
        senha = input(f"Digite a sua senha ADM: ")
        senha_criptografada = sha256(senha.encode()).hexdigest()
        
        if senha_criptografada in adm_senha:
            
            print("Bem-vindo ADM")
            
        else:
            print("Senha incorreta tente novamente")
            autentificacao()
        
    elif login in usuario_logins:
        
        id = int(input(f"Digite o seu ID: "))
        
        if id in usuario_senha: 
            
            print("Bem-vindo usuário")
            
        else:
            print("ID errado tente novamente")
            autentificacao()
        
    else:      
        print("Login inválido tente novamente")
        autentificacao()
'''












'''
def autenticacao(login, senha):
        armazenamento_de_usuarios = f'SELECT FROM * administrador WHERE login'
        armazenamento_de_senhas = f'SELECT FROM * administrador WHERE senha'
        cursor.execute(armazenamento_de_usuarios, armazenamento_de_senhas)
        cursor.fetchall()

        for login in armazenamento_de_usuarios:
            if login == login:
                for senha in armazenamento_de_senhas:
                    if senha == senha: 
                        print("Login efetuado com sucesso")
'''