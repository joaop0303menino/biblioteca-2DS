#Ignorem o main pq eu estou usando para testes
import flet as ft
import usuario as user

# Função para ler a tabela do SQL Server e retornar uma DataTable do Flet
def read_table_user():
    read_table = user.ver_usuario()

    headers = [ft.DataColumn(ft.Text(col)) for col in read_table.columns]
    rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(str(value))) for value in row]) for row in read_table.values]

    data_table = ft.DataTable(columns=headers, rows=rows)

    return data_table

data_table_ = read_table_user()

def pagina_principal(pagina: ft.Page):
    def update_table(e):
        pagina.controls.clear()
        tabela = read_table_user()
        pagina.add(tabela, ft.ElevatedButton('Atualizar tabela', on_click=update_table))
        pagina.update()

    def update_id(e):
        pagina.go('/update_id')
        nonlocal click_bt
        click_bt = 'id'
    
    click_bt = ''

    bt_opcao_id = ft.ElevatedButton('Atualizar id', on_click=update_id)

    pagina.add(bt_opcao_id)

  

    def abas(e):
        pagina.views.clear()
        if pagina.route == '/update_id':
            pagina.views.append(
                ft.View(
                    '/update_id',
                    controls=[
                        data_table_,
                        ft.ElevatedButton('Atualizar tabela', on_click=update_table)
                    ],
                )
            )
            pagina.update()

    pagina.on_route_change = abas
    abas(None)

#ft.app(target=pagina_principal)