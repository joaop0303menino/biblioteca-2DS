import integracao_sql
import pandas as pd
from datetime import datetime, timedelta


integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def ver_historico():
    
    tabela = pd.read_sql(f'select * from historico',conexao)  
    print(tabela)
    