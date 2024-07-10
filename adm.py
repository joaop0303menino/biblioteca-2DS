import integracao_sql
import pandas as pd

integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def ver_administrador():
    
    tabela = pd.read_sql(f'select * from administrador',conexao)  
    print(tabela)

def inserir_administrador():
    
    print(f"pressione enter para continuar \npara sair digite '!n'")
    dados = ""
    
    while dados != "!n":
        dados = input('Deseja continuar: ')
        
        if dados != "!n":
        
            id = int(input(f'Digite o código do administrador: '))
            login = input(f'Digite o login do administrador: ')
            senha = input(f'Digite a senha de administrador: ')
            senha_criptografada = sha256(senha.encode()).hexdigest()
            
            cursor.execute(f"insert into administrador(id,login,senha) values (?,?,?)",(id,login,senha_criptografada))
            cursor.commit()  
        else:   
            ver_administrador()