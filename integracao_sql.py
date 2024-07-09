import pyodbc 

def  juncao_sql():
    dados_conexao = (
        'DRIVER={SQL Server};'
        'Server=DESKTOP-JHQABHK;'
        'DATABASE=dados da biblioteca;'
    )

    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    return cursor, conexao
    print('Conexão sucedida')
    


