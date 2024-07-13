import integracao_sql
import pandas as pd
from hashlib import sha256

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
            
def atualizar_administrador():
    
    ver_administrador()
    
    print("Digite o número da opção que deseja alterar")
    print(f"1) ID do administrador\n 2) login do administrador\n 3) senha de administrador")
    escolha = int(input("qual opção você deseja: "))
    
    opcao = ''
    mudanca = input(f"Digite a sua Alteração: ")
    Oq_mudar = input(f"Digite o ID do administrador que deseja alterar: ")
    
    if escolha == 1:
        opcao = 'id'
    elif escolha == 2:
        opcao = 'login'
    elif escolha == 3: 
        opcao = 'senha'
    else:
        print("Opção inválida tente novamente")
        atualizar_administrador() 
        
    cursor.execute(f"update administrador set {opcao} = ? where id = ?",(mudanca, Oq_mudar))
    cursor.commit()  
    
    ver_administrador()
    
def deletar_administrador():
    
    ver_administrador()
    
    id = input("Digite o ID do administrador que deseja deletar: ")
    
    cursor.execute(f" delete from administrador where id = {id}")
    cursor.commit()
    
    ver_administrador()