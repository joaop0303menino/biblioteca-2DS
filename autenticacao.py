import integracao_sql as sql
import pyodbc as dbc
from hashlib import sha256
    
login_adm = 0
login_user = 1

def verificar_user_ou_adm(login):
    cursor, conexao = sql.juncao_sql()

    cursor.execute("select login from administrador")
    adm_logins = [row[0] for row in cursor.fetchall()]
        
    cursor.execute("select nome from usuario")
    usuario_logins = [row[0] for row in cursor.fetchall()]
        
    if login in adm_logins:
        return True
        
    elif login in usuario_logins:
       return False
    else:      
        print("Login inválido tente novamente")
        return False

def autenticar(login, senha):
    cursor, conexao = sql.juncao_sql()

    cursor.execute("select login from administrador")
    adm_logins = [row[0] for row in cursor.fetchall()]
        
    cursor.execute("select nome from usuario")
    usuario_logins = [row[0] for row in cursor.fetchall()]
    
    cursor.execute(f"select senha from administrador where login = ?",(login))
    adm_senha = [row[0] for row in cursor.fetchall()]
    
    cursor.execute(f"select senha from usuario where nome = ?",(login))
    usuario_senha = [row[0] for row in cursor.fetchall()]
        
    if login in adm_logins:
        
        senha_criptografada = sha256(senha.encode()).hexdigest()

        if senha_criptografada in adm_senha:
            print("Bem-vindo ADM")
            return True, login_adm

        else:
            print("Senha incorreta tente novamente")
            return False
        
    elif login in usuario_logins:
        if senha in usuario_senha: 
            print("Bem-vindo usuário")
            return True, login_user

        else:
            print("ID errado tente novamente")
            return False
        
    else:      
        print("Login inválido tente novamente")
        return False