import integracao_sql
import pandas as pd
import flet as ft

integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def read_table_user():
    read_table = pd.read_sql(f'select * from usuario',conexao)

    headers = [ft.DataColumn(ft.Text(col)) for col in read_table.columns]
    rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(str(value))) for value in row]) for row in read_table.values]

    data_table = ft.DataTable(columns=headers, rows=rows)

    return data_table
    
def inserir_usuario(id,nome,sobrenome):
        cursor.execute(f"insert into usuario(id,nome,sobrenome) values ({id},'{nome}','{sobrenome}')")
        cursor.commit()

def atualizar_usuario(opcao,mudanca,Oq_mudar):
    query = f"UPDATE usuario SET {opcao} = ? WHERE id = ?"
    cursor.execute(query, (mudanca, Oq_mudar))
    cursor.commit()

    txt_confirmation_update = 'Usuário atualizado com sucesso'
    return txt_confirmation_update 
    
def deletar_usuario(id_usuario):
    cursor.execute(f" delete from usuario where id = {id_usuario}")
    cursor.commit()
    
    txt_confirmation_remove = 'Usuário removido com sucesso'
    return txt_confirmation_remove

def verificar_usuario_existe(valor):
    query = f'SELECT * FROM usuario'
    cursor.execute(query)
    id_user = [row[0] for row in cursor.fetchall()]
    if valor in id_user:
        print(True)
        return True
    else:      
        print(False)
        return False