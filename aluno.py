import integracao_sql
import pandas as pd

integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def ver_aluno():
    
    tabela = pd.read_sql(f'select * from aluno',conexao)  
    print(tabela)
    
def inserir_aluno():
    
    print(f"pressione enter para continuar \npara sair digite '!n'")
    dados = ""
    
    while dados != "!n":
        dados = input('Deseja continuar: ')
        
        if dados != "!n":
        
            ra = input(f'Digite o RA do aluno: ')
            nome = input(f'Digite o nome do aluno: ')
            sobrenome = input(f"Digite o sobrenome do aluno: ")
            serie = input(f'Digite a série do aluno: ')
            
            cursor.execute(f"insert into aluno(RA,nome,sobrenome,serie) values ({ra},'{nome}','{sobrenome}','{serie}')")
            cursor.commit()  
        else:   
            ver_aluno()
            
def atualizar_aluno():
    
    ver_aluno()
    
    print("Digite o número da opção que deseja alterar")
    print(f"1) RA do aluno\n 2) Nome do aluno\n 3) sobrenome do aluno\n 4) série do aluno")
    escolha = int(input("qual opção você deseja: "))
    
    opcao = ''
    mudanca = input(f"Digite a sua Alteração: ")
    Oq_mudar = input(f"Digite o RA do aluno que deseja alterar: ")
    
    if escolha == 1:
        opcao = 'RA'
    elif escolha == 2:
        opcao = 'nome'
    elif escolha == 3: 
        opcao = 'sobrenome'
    elif escolha == 4:
        opcao = 'serie'
    else:
        print("Opção inválida tente novamente")
        atualizar_aluno() 
        
    cursor.execute(f"update aluno set {opcao} = ? where RA = ?",(mudanca, Oq_mudar))
    cursor.commit()  
    
    ver_aluno()