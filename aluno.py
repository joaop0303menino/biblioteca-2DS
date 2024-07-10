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