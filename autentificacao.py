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
        