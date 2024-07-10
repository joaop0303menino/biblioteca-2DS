import integracao_sql
import pandas as pd

integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def ver_livros():
    
    tabela = pd.read_sql(f'select * from livro',conexao)  
    print(tabela)
  
def inserir_livros():
    
    print(f"pressione enter para continuar \npara sair digite '!n'")
    dados = ""
    
    while dados != "!n":
        dados = input('Deseja continuar: ')
        
        if dados != "!n":
        
            codigo = int(input(f'Digite o código do livro: '))
            nome = input(f'Digite o nome do livro: ')
            quantidade = int(input(f'Digite a quantidade de livros: '))
            
            cursor.execute(f"insert into livro(codigo,nome,quantidade) values ({codigo},'{nome}',{quantidade})")
            cursor.commit()  
        else:   
            ver_livros()
