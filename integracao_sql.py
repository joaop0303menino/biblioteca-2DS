import pyodbc 

def  juncao_sql():
    dados_conexao = (
        'DRIVER={SQL Server};'
        'Server=Bruno;'
        'DATABASE=dados da biblioteca;'
    )

    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    return cursor, conexao
