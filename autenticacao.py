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
        
        senha_criptografada = sha256(senha.encode()).hexdigest()

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