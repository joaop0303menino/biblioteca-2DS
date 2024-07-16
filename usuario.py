import integracao_sql
import pandas as pd
import flet as ft

cursor, conexao = integracao_sql.juncao_sql()
    
def inserir_usuario(id,nome,sobrenome):
        cursor.execute(f"insert into usuario(id,nome,sobrenome) values ({id},'{nome}','{sobrenome}')")
        cursor.commit()

def atualizar_usuario(opcao,mudanca,Oq_mudar):
    query = f"UPDATE usuario SET {opcao} = ? WHERE id = ?"
    cursor.execute(query, (mudanca, Oq_mudar))
    cursor.commit()

    txt_confirmation_update = 'Usuário atualizado com sucesso'
    return txt_confirmation_update 