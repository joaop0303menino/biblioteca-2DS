import integracao_sql
import pandas as pd

integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def ver_administrador():
    
    tabela = pd.read_sql(f'select * from administrador',conexao)  
    print(tabela)
