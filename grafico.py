import flet as ft
import autenticacao as aut
import adm 
import aluno as al
import historico as his
import livros as li
import usuario as user
import funcoes_globais as defs
from functools import lru_cache

@lru_cache
def pagina_principal(pagina: ft.Page):
    pagina.title = 'Biblioteca CG'
    pagina.window_width = 1920
    pagina.window_height = 1080

    def menu_main(e):
        pagina.go('/menu')

    bt_menu_main = ft.ElevatedButton('Menu do sistema', on_click=menu_main)
    
    # Página principal:
    text_bem_vindo = ft.Text('Bem vindo à biblioteca do Carlos Gomes')
    text_explicacao1 = ft.Text('Este sistema foi feito para os administradores e responsáveis da biblioteca')
    text_explicacao2 = ft.Text('Aqui você pode cadastrar livros, usuários e permitir que alunos peguem livros com mais segurança')
    
    login_inserido = ft.TextField(label='Insira seu login de ADM ou Usuário')
    senha_inserida = ft.TextField(label='Insira a sua senha de ADM ou o ID de usuário:', password=True, on_submit= menu_main)
    
    #Botão para trocar o tema da pagina
    def tema(bt_tema):
        if bt_tema.value == True:
            pagina.theme_mode = 'light'
        else:
            pagina.theme_mode = 'dark'
        pagina.update()

    bt_tema = ft.Switch(
        label="Cor do tema",
        value=False,
        thumb_color={ft.ControlState.SELECTED: ft.colors.WHITE},
        track_color=ft.colors.BLACK,
        on_change=lambda e: tema(bt_tema),
    )

    def login(e):
        login_valor = login_inserido.value
        senha_valor = senha_inserida.value

        if aut.autenticar(login_valor, senha_valor):
            menu_main(e)
        else:
            pagina.add(ft.Text('Login e/ou senha incorretos.'))
            pagina.update()

    entrar = ft.ElevatedButton(text='Entrar', on_click=login)

    #Baner caso o usuário queria entrar nas funções feitas só para os adms
    def fechar_banner(e):
        banner.open = False
        pagina.update()

    banner = ft.Banner(
        bgcolor=ft.colors.BLACK,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.RED, size=40),
        content=ft.Text(
            value="Para acessar este local você precisa ser administrador",
            color=ft.colors.WHITE),
        actions=[ft.TextButton(text="Voltar para o menu", on_click=fechar_banner)]
    )

    #Funções dos botões do menu
    def menu_user(e):
        login_valor = login_inserido.value

        if aut.verificar_user_ou_adm(login_valor):
            pagina.go('/menu_user')
        else:
            pagina.add(banner)
            pagina.update()
    
    bt_menu_user = ft.ElevatedButton('Menu do usuário', on_click=menu_user)

    def menu_adm(e):
        login_valor = login_inserido.value

        if aut.verificar_user_ou_adm(login_valor):
            pagina.go('/menu_adm')
        else:
            pagina.add(banner)
            pagina.update()

    bt_menu_adm = ft.ElevatedButton('Menu administrador', on_click=menu_adm)

    def menu_aluno(e):
        pagina.go('/menu_aluno')

    bt_menu_aluno = ft.ElevatedButton('Menu aluno', on_click=menu_aluno)

    def menu_livro(e):
        pagina.go('/menu_livro')

    bt_menu_livro = ft.ElevatedButton('Menu livro', on_click=menu_livro)

    def menu_historico(e):
        pagina.go('/menu_histórico')

    bt_menu_historico = ft.ElevatedButton('Menu histórico', on_click=menu_historico)

    def emprestar_livro(e):
        pagina.go('/emprestar_livro')

    bt_aba_emprestar_livro = ft.ElevatedButton('Emprestar livro', on_click=emprestar_livro)

    def sair(e):
        pagina.go('/')

    bt_sair = ft.ElevatedButton('Sair do sistema', on_click=sair)

    # Funções dos botões do menu_user
    def create_user(e):
        pagina.go('/create_user')
    
    def update_user(e):
        pagina.go('/update_user')
    
    def read_user(e):
        pagina.go('/read_user')
    
    def remove_user(e):
        pagina.go('/remove_user')

    #Informações para adicionar o usuário
    def update_id(e):
        nonlocal click_id
        click_id = 'id'
        pagina.go('/update_id')
    click_update_user = click_id = ''

    def update_nome(e):
        nonlocal click_nome
        click_nome = 'nome'
        pagina.go('/update_nome')
    click_update_user = click_nome = ''
    
    def update_sobrenome(e):
        nonlocal click_sobrenome
        click_sobrenome = 'sobrenome'
        pagina.go('/update_sobrenome')
    click_update_user = click_sobrenome = ''

    txt_id = ft.TextField(label='Id:')
    txt_nome = ft.TextField(label='Nome:')
    txt_sobrenome = ft.TextField(label='Sobrenome:')

    #Informações para atulizar o usuário
    bt_opcao_id = ft.ElevatedButton('Atualizar id', on_click=update_id)
    bt_opcao_nome = ft.ElevatedButton('Atualizar nome', on_click=update_nome)
    bt_opcao_sobrenome = ft.ElevatedButton('Atualizar sobrenome', on_click=update_sobrenome)

    #Informações para atualizar o id
    input_id_atual = ft.TextField(label='Insira o id atual:')
    input_id_atualizado = ft.TextField(label='Insira o id atulizado:')
    bt_update_id = ft.ElevatedButton('Atualizar id', on_click=lambda _: user.atualizar_usuario(click_id,input_id_atual.value, input_id_atualizado.value))

    #Informações para atualizar o nome
    input_nome_atual = ft.TextField(label='Insira o nome atual:')
    input_nome_atualizado = ft.TextField(label='Insira o nome atulizado:')
    bt_update_nome = ft.ElevatedButton('Atualizar nome', on_click=lambda _: user.atualizar_usuario(click_nome,input_nome_atual.value, input_nome_atualizado.value))

    #Informações para atualizar o sobrenome
    input_sobrenome_atual = ft.TextField(label='Insira o sobrenome atual:')
    input_sobrenome_atualizado = ft.TextField(label='Insira o sobrenome atulizado:')
    bt_update_sobrenome = ft.ElevatedButton('Atualizar sobrenome', on_click=lambda _: user.atualizar_usuario(click_sobrenome,input_sobrenome_atual.value, input_sobrenome_atualizado.value))

    #Informações para ver a tabela
    #read_table = defs.read_table()
    read_table_user = defs.read_table(click_update_user)


    #bt_read_table_user = ft.ElevatedButton('Ver tabela', on_click=read_table_user)

    def update_table(e):
        if read_table_user in pagina.controls:
            pagina.remove(read_table_user)
        read_table_user
        pagina.add(read_table_user)
        pagina.update()

    bt_update_table_user = ft.ElevatedButton('Atualizar tabela', on_click=update_table)

    #Informações para remover 
    def remover_usuario(e):
        opcao = user.verificar_usuario_existe(input_remove_user.value)
        if not opcao == True:
            txt_confirmation_remove.value = 'Insira um id válido.'
        else:
            mensagem = user.deletar_usuario(input_remove_user.value)
            txt_confirmation_remove.value = mensagem
        pagina.update()

    bt_remove_user = ft.ElevatedButton('Remover usuário', on_click=remover_usuario)
    input_remove_user = ft.TextField(label= 'Insira o id do usuário que você deseja remover', on_submit=bt_remove_user)
    txt_confirmation_remove = ft.Text()

    #Emprestar livro
    bt_emprestar_livro = ft.ElevatedButton('Emprestar livro', '''on_click=inserir a função emprestar livro''')
    RA = ft.TextField(label='Adicione o RA do aluno:')
    codigo_livro = ft.TextField(label='Qual o código do livro:')
    obs = ft.TextField(label='Observação do livro(se ele está danificado ou não, qual o nível de danificação):', on_submit=bt_emprestar_livro)
    
    def abas(e):
        pagina.views.clear()
        if pagina.route == '/':
            pagina.views.append(
                ft.View(
                    '/',
                    controls=[
                        ft.Row(
                            controls=[
                                text_bem_vindo,
                                bt_tema,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        text_explicacao1,
                        text_explicacao2,
                        login_inserido,
                        senha_inserida,
                        entrar
                    ],
                )
            )
        elif pagina.route == '/menu':
            pagina.views.append(
                ft.View(
                    '/menu',
                    controls=[
                        ft.AppBar(title=ft.Text('Menu'), bgcolor=ft.colors.SURFACE_VARIANT),
                        bt_menu_user,
                        bt_menu_adm,
                        bt_menu_aluno,
                        bt_menu_livro,
                        bt_menu_historico,
                        bt_aba_emprestar_livro,
                        bt_sair,
                    ],
                )
            )
        elif pagina.route == '/menu_user':
            pagina.views.append(
                ft.View(
                    '/menu_user',
                    controls=[
                        ft.AppBar(title=ft.Text('Menu usuário\nEscolha uma opção:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton('Adicionar usuário', on_click=create_user),
                        ft.ElevatedButton('Atualizar usuário', on_click=update_user),
                        ft.ElevatedButton('Ver todos os usuários', on_click=read_user),
                        ft.ElevatedButton('Remover usuário', on_click=remove_user),
                        bt_menu_main,
                        bt_sair,
                    ],
                )
            )
        elif pagina.route == '/create_user':
            pagina.views.append(
                ft.View(
                    '/create_user',
                    controls=[
                        ft.AppBar(title=ft.Text('Adicionar usuário\nInsira as seguintes informações:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        txt_id,
                        txt_nome,
                        txt_sobrenome,
                        ft.ElevatedButton('Adicionar usuário', on_click=lambda _:user.inserir_usuario(txt_id.value, txt_nome.value, txt_sobrenome.value)),
                        read_table_user,
                        bt_update_table_user,
                        bt_menu_user,
                        bt_menu_main,
                        bt_sair,
                    ],
                )
            )
        elif pagina.route == '/update_user':
            pagina.views.append(
                ft.View(
                    '/update_user',
                    controls=[
                        ft.AppBar(title=ft.Text('Atualizar usuário\nClique na opção que deseja mudar'), bgcolor=ft.colors.SURFACE_VARIANT),
                        bt_opcao_id,
                        bt_opcao_nome,
                        bt_opcao_sobrenome,
                        bt_menu_user,
                        bt_menu_main,
                        bt_sair,
                    ],
                )
            )
        elif pagina.route == '/update_id':
            pagina.views.append(
                ft.View(
                    '/update_id',
                    controls=[
                        ft.AppBar(title=ft.Text('Atualizar id\nInsira as informações:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        read_table_user,
                        bt_update_table_user,
                        input_id_atual,
                        input_id_atualizado,
                        bt_update_id,
                        bt_menu_user,
                        bt_menu_main,
                        bt_sair,
                    ],
                )
            )
        elif pagina.route == '/update_nome':
            pagina.views.append(
                ft.View(
                    '/update_nome',
                    controls=[
                        ft.AppBar(title=ft.Text('Atualizar usuário\nClique na opção que deseja mudar'), bgcolor=ft.colors.SURFACE_VARIANT),
                        read_table_user,
                        bt_update_table_user,
                        input_nome_atual,
                        input_nome_atualizado,
                        bt_update_nome,
                        bt_menu_user,
                        bt_menu_main,
                        bt_sair,
                    ],
                )
            )
        elif pagina.route == '/update_sobrenome':
            pagina.views.append(
                ft.View(
                    '/update_sobrenome',
                    controls=[
                        ft.AppBar(title=ft.Text('Atualizar usuário\nClique na opção que deseja mudar'), bgcolor=ft.colors.SURFACE_VARIANT),
                        read_table_user,
                        bt_update_table_user,
                        input_sobrenome_atual,
                        input_sobrenome_atualizado,
                        bt_update_sobrenome,
                        bt_menu_user,
                        bt_menu_main,
                        bt_sair,
                    ],
                )
            )
        elif pagina.route == '/read_user':
            pagina.views.append(
                ft.View(
                    '/read_user',
                    controls=[
                        ft.AppBar(title=ft.Text('Ver todos os usuários:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        read_table_user,
                        update_table,
                        bt_menu_user,
                        bt_menu_main,
                        bt_sair,
                    ],
                )
            )
        elif pagina.route == '/remove_user':
            pagina.views.append(
                ft.View(
                    '/remove_user',
                    controls=[
                        ft.AppBar(title=ft.Text('Remover usuário\nInsira as seguintes informações:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        input_remove_user,
                        bt_remove_user,
                        txt_confirmation_remove,
                        read_table_user,
                        bt_update_table_user,
                        bt_menu_user,
                        bt_menu_main,
                        bt_sair,
                    ],
                )
            )
        elif pagina.route == '/menu_adm':
            pagina.views.append(
                ft.View(
                    '/menu_adm',
                    controls=[
                        ft.AppBar(title=ft.Text('Menu administrador\nEscolha uma opção:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton('Adicionar administrador'),
                        ft.ElevatedButton('Atualizar administrador'),
                        ft.ElevatedButton('Ver todos os administradores'),
                        ft.ElevatedButton('Remover administrador'),
                        bt_menu_adm,
                        bt_menu_main,
                        bt_sair,
                    ],
                )
            )
        elif pagina.route == '/menu_aluno':
            pagina.views.append(
                ft.View(
                    '/menu_aluno',
                    controls=[
                        ft.AppBar(title=ft.Text('Menu aluno\nEscolha uma opção:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton('Adicionar aluno'),
                        ft.ElevatedButton('Atualizar aluno'),
                        ft.ElevatedButton('Ver todos os alunos'),
                        ft.ElevatedButton('Remover aluno'),
                        bt_menu_aluno,
                        bt_menu_main,
                        bt_sair,
                    ],
                )
            )
        elif pagina.route == '/menu_livro':
            pagina.views.append(
                ft.View(
                    '/menu_livro',
                    controls=[
                        ft.AppBar(title=ft.Text('Menu livro\nEscolha uma opção:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton('Adicionar livro'),
                        ft.ElevatedButton('Atualizar livro'),
                        ft.ElevatedButton('Ver todos os livros'),
                        ft.ElevatedButton('Remover livro'),
                        bt_menu_livro,
                        bt_menu_main,
                        bt_sair,
                    ],
                )
            )
        elif pagina.route == '/menu_histórico':
            pagina.views.append(
                ft.View(
                    '/menu_histórico',
                    controls=[
                        ft.AppBar(title=ft.Text('Menu histórico\nEscolha uma opção:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton('Ver histórico de aluno'),
                        ft.ElevatedButton('Ver histórico de livro'),
                        ft.ElevatedButton('Ver histórico geral'),
                        bt_menu_historico,
                        bt_menu_main,
                        bt_sair,
                    ],
                )
            )
        elif pagina.route == '/emprestar_livro':
            pagina.views.append(
                ft.View(
                    '/emprestar_livro',
                    controls=[
                        ft.AppBar(title=ft.Text('Emprestar livro\nLembre que o aluno tem que estar cadastrado\nInsira as seguintes informações:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        RA,
                        codigo_livro,
                        obs,
                        bt_emprestar_livro,
                        bt_menu_main,
                        bt_sair,
                    ],
                )
            )
        pagina.update()
    
    pagina.add(ft.Text('\n'), bt_menu_main)
    pagina.update()
    
    pagina.on_route_change = abas
    abas(None)

def init_main():
    ft.app(target=pagina_principal)

init_main()