import integracao_sql
import pandas as pd

cursor, conexao = integracao_sql.juncao_sql()

def inserir_aluno(ra,nome,sobrenome,serie,continuar):
    
    print(f"pressione enter para continuar \npara sair digite '!n'")
    continuar = ""
    
    while continuar != "!n":
        continuar = input('Deseja continuar: ')
        
        if continuar != "!n":

            cursor.execute(f"insert into aluno(RA,nome,sobrenome,serie) values ({ra},'{nome}','{sobrenome}','{serie}')")
            cursor.commit()  
        else:   
            ver_aluno()
            
def atualizar_aluno(escolha,mudanca,Oq_mudar,opcao):
    
    ver_aluno()
    
    print("Digite o número da opção que deseja alterar")
    print(f"1) RA do aluno\n 2) Nome do aluno\n 3) sobrenome do aluno\n 4) série do aluno")
    
    opcao = ''
    
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
    
def deletar_aluno(ra):
    
    ver_aluno()
    
    cursor.execute(f" delete from aluno where RA = {ra}")
    cursor.commit()
    
    ver_aluno()