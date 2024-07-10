import integracao_sql
import pandas as pd

integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def ver_usuario():
    
    tabela = pd.read_sql(f'select * from usuario',conexao)  
    print(tabela)