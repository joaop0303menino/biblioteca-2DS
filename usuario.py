import integracao_sql
import pandas as pd

integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def ver_usuario():
    
    tabela = pd.read_sql(f'select * from usuario',conexao)  
    print(tabela)
    
def inserir_usuario(id_usuario,nome,sobrenome,continuar):
    
    print(f"pressione enter para continuar \npara sair digite '!n'")
    continuar = ""
    
    while continuar != "!n":
        continuar = input('Deseja continuar: ')
        
        if continuar != "!n":

            cursor.execute(f"insert into usuario(id,nome,sobrenome) values ({id},'{nome}','{sobrenome}')")
            cursor.commit()  
            
        else:   
            ver_usuario()

def atualizar_usuario(escolha,mudanca,Oq_mudar,opcao):
    
    ver_usuario()
    
    print("Digite o número da opção que deseja alterar")
    print(f"1) ID do usuario\n 2) Nome do usuario\n 3) sobrenome de usuario")
    
    opcao = ''
    
    
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
    
def deletar_usuario(id_usuario):
    
    ver_usuario()
    
    cursor.execute(f" delete from usuario where id = {id_usuario}")
    cursor.commit()
    
    ver_usuario()