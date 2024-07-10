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