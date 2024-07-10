import integracao_sql
import pandas as pd

integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def ver_livros():
    
    tabela = pd.read_sql(f'select * from livro',conexao)  
    print(tabela)

ver_livros()