import flet as ft
import autenticacao as aut
import adm 
import aluno as al
import historico as his
import livros as li
import usuario as user

def pagina_principal(pagina: ft.Page):
    pagina.title = 'Biblioteca CG'
    pagina.window_width = 1920
    pagina.window_height = 1080

    def menu_main(e):
        pagina.go('/menu')
    
    # Página principal:
    text_bem_vindo = ft.Text('Bem vindo à biblioteca do Carlos Gomes')
    text_explicacao1 = ft.Text('Este sistema foi feito para os administradores e responsáveis da biblioteca')
    text_explicacao2 = ft.Text('Aqui você pode cadastrar livros, usuários e permitir que alunos peguem livros com mais segurança')
    
    login_inserido = ft.TextField(label='Insira seu login de ADM ou Usuário')
    senha_inserida = ft.TextField(label='Insira a sua senha de ADM ou o ID de usuário:', password=True, on_submit= menu_main)

    #Emprestar livro
    RA = ft.TextField(label='Adicione o RA do aluno:')
    codigo_livro = ft.TextField(label='Qual o código do livro:')
    obs = ft.TextField(label='Observação do livro(se ele está danificado ou não, qual o nivel de danificação):')

    def fechar_banner(e):
        banner.open = False
        pagina.update()

    banner = ft.Banner(
        bgcolor=ft.colors.BLACK,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.RED, size=40),
        content=ft.Text(
        value="Para acessar este local você precisa ser administrador",
        color=ft.colors.WHITE),
        actions=[ft.TextButton(text="Voltar para o menu", on_click=fechar_banner)])

    def menu_user(e):
        login_valor = login_inserido.value

        if aut.verificar_user_ou_adm(login_valor) == True:
            pagina.go('/Menu_user')
        elif aut.verificar_user_ou_adm(login_valor) == False:
            pagina.add(pagina.open(banner))

    def menu_aluno(e):
        pagina.go('/menu_aluno')

    def menu_livro(e):
        pagina.go('/menu_livro')

    def menu_historico(e):
        pagina.go('/menu_historico')

    def emprestar_livro(e):
        pagina.go('/Emprestar_livro')

    def sair(e):
        pagina.go('/')

    def login(e):
        login_valor = login_inserido.value
        senha_valor = senha_inserida.value

        if aut.autenticar(login_valor, senha_valor):
            menu_main(e)
        else:
            pagina.add(ft.Text('Login e/ou senha incorretos.'))
            pagina.update()

    entrar = ft.ElevatedButton(text='Entrar', on_click=login)

    def abas(e):
        pagina.views.clear()
        if pagina.route == '/':
            pagina.views.append(
                ft.View(
                    '/',
                    [
                        text_bem_vindo,
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
                    [
                        ft.AppBar(title=ft.Text('Menu'), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton('Menu usuário', on_click=menu_user),
                        ft.ElevatedButton('Menu aluno', on_click=menu_aluno),
                        ft.ElevatedButton('Menu livro', on_click=menu_livro),
                        ft.ElevatedButton('Menu histórico', on_click=menu_historico),
                        ft.ElevatedButton('Emprestar livro', on_click=emprestar_livro),
                        ft.ElevatedButton('Sair do sistema', on_click=sair),
                    ],
                )
            )
        elif pagina.route == '/Menu_user':
            pagina.views.append(
                ft.View(
                    '/Menu_user',
                    [
                        ft.AppBar(title=ft.Text('Menu usuário\nEscolha uma opção:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton('Adicionar usuário'),
                        ft.ElevatedButton('Atualizar usuário'),
                        ft.ElevatedButton('Ver todos os usuários'),
                        ft.ElevatedButton('Remover usuário'),
                        ft.ElevatedButton('Menu do sistema', on_click=menu_main),
                    ],
                )
            )
        elif pagina.route == '/Menu_aluno':
            pagina.views.append(
                ft.View(
                    '/Menu_aluno',
                    [
                        ft.AppBar(title=ft.Text('Menu aluno\nEscolha uma opção:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton('Adicionar aluno'),
                        ft.ElevatedButton('Atualizar aluno'),
                        ft.ElevatedButton('Ver todos os alunos'),
                        ft.ElevatedButton('Remover aluno'),
                        ft.ElevatedButton('Menu do sistema', on_click=menu_main),
                    ],
                )
            )
        elif pagina.route == '/Menu_livro':
            pagina.views.append(
                ft.View(
                    '/Menu_livro',
                    [
                        ft.AppBar(title=ft.Text('Menu livro\nEscolha uma opção:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton('Adicionar livro'),
                        ft.ElevatedButton('Atualizar livro'),
                        ft.ElevatedButton('Ver todos os livros'),
                        ft.ElevatedButton('Remover livro'),
                        ft.ElevatedButton('Menu do sistema', on_click=menu_main),
                    ],
                )
            )
        elif pagina.route == '/Menu_histórico':
            pagina.views.append(
                ft.View(
                    '/Menu_histórico',
                    [
                        ft.AppBar(title=ft.Text('Menu histórico\nEscolha uma opção:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton('Atualizar histórico'),
                        ft.ElevatedButton('Ver todo o histórico', on_click=his.ver_historico),
                        ft.ElevatedButton('Remover histórico'),
                        ft.ElevatedButton('Menu do sistema', on_click=menu_main),
                    ],
                )
            )
        elif pagina.route == '/Emprestar_livro':
            pagina.views.append(
                ft.View(
                    '/Emprestar_livro',
                    [
                        ft.AppBar(title=ft.Text('Menu usuário\nPara emprestar um livro digite as seguintes informações:'), bgcolor=ft.colors.SURFACE_VARIANT),
                        RA,
                        codigo_livro,
                        obs,
                        ft.ElevatedButton('Emprestar livro', on_click=lambda _:his.inserir_historico(RA.value, codigo_livro.value, obs.value,)),
                        ft.ElevatedButton('Menu do sistema', on_click=menu_main),
                    ],
                )
            )

        pagina.update()

    def view_pop(e):
        pagina.views.pop()
        top_view = pagina.views[-1]
        pagina.go(top_view.route)

    pagina.on_route_change = abas
    pagina.on_view_pop = view_pop

    pagina.go(pagina.route)

def init_app():
    ft.app(target=pagina_principal, view=ft.WEB_BROWSER)

init_app()