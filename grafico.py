import flet as ft
import autenticacao as aut

def pagina_principal(pagina: ft.Page):
    pagina.title = 'Biblioteca CG'
    pagina.window_width = 1920
    pagina.window_height = 1080

    # Página principal:
    text_bem_vindo = ft.Text('Bem vindo à biblioteca do Carlos Gomes')
    text_explicacao1 = ft.Text('Este sistema foi feito para os administradores e responsáveis da biblioteca')
    text_explicacao2 = ft.Text('Aqui você pode cadastrar livros, usuários e permitir que alunos peguem livros com mais segurança')
    
    login_inserido = ft.TextField(label='Insira seu login de ADM ou Usuário')
    senha_inserida = ft.TextField(label='Insira a sua senha de ADM ou o ID de usuário:', password=True)

    def menu_main(e):
        pagina.go('/menu')

    def menu_user(e):
        pagina.go('/Menu_user')

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
                        ft.ElevatedButton('Menu aluno'),
                        ft.ElevatedButton('Menu livro'),
                        ft.ElevatedButton('Ver histórico'),
                        ft.ElevatedButton('Emprestar livro'),
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

        pagina.update()

    def view_pop(e):
        pagina.views.pop()
        top_view = pagina.views[-1]
        pagina.go(top_view.route)

    pagina.on_route_change = abas
    pagina.on_view_pop = view_pop

    pagina.go(pagina.route)

ft.app(target=pagina_principal, view=ft.WEB_BROWSER)

