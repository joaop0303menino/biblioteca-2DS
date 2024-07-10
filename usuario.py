import integracao_sql
import pandas as pd

integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def ver_usuario():
    
    tabela = pd.read_sql(f'select * from usuario',conexao)  
    print(tabela)
    
def inserir_usuario():
    
    print(f"pressione enter para continuar \npara sair digite '!n'")
    dados = ""
    
    while dados != "!n":
        dados = input('Deseja continuar: ')
        
        if dados != "!n":
        
            id = int(input(f'Digite o código do usuario: '))
            nome = input(f'Digite o nome do usuario: ')
            sobrenome = input(f'Digite a sobrenome de usuario: ')
            
            cursor.execute(f"insert into usuario(id,nome,sobrenome) values ({id},'{nome}','{sobrenome}')")
            cursor.commit()  
        else:   
            ver_usuario()

def atualizar_usuario():
    
    ver_usuario()
    
    print("Digite o número da opção que deseja alterar")
    print(f"1) ID do usuario\n 2) Nome do usuario\n 3) sobrenome de usuario")
    escolha = int(input("qual opção você deseja: "))
    
    opcao = ''
    mudanca = input(f"Digite a sua Alteração: ")
    Oq_mudar = input(f"Digite o ID do usuario que deseja alterar: ")
    
    if escolha == 1:
        opcao = 'id'
    elif escolha == 2:
        opcao = 'nome'
    elif escolha == 3: 
        opcao = 'sobrenome'
    else:
        print("Opção inválida tente novamente")
        atualizar_usuario() 
        
    cursor.execute(f"update usuario set {opcao} = ? where id = ?",(mudanca, Oq_mudar))
    cursor.commit()  
    
    ver_usuario()