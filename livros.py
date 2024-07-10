import integracao_sql
import pandas as pd

integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def ver_livros():
    
    tabela = pd.read_sql(f'select * from livro',conexao)  
    print(tabela)
  
def inserir_livros():
    
    print(f"pressione enter para continuar \npara sair digite '!n'")
    dados = ""
    
    while dados != "!n":
        dados = input('Deseja continuar: ')
        
        if dados != "!n":
        
            codigo = int(input(f'Digite o código do livro: '))
            nome = input(f'Digite o nome do livro: ')
            quantidade = int(input(f'Digite a quantidade de livros: '))
            
            cursor.execute(f"insert into livro(codigo,nome,quantidade) values ({codigo},'{nome}',{quantidade})")
            cursor.commit()  
        else:   
            ver_livros()

def atualizar_livro():
    
    ver_livros()
    
    print("Digite o número da opção que deseja alterar")
    print(f"1) Código do livro\n 2) Nome do livro\n 3) Quantidade de livro")
    escolha = int(input("qual opção você deseja: "))
    
    opcao = ''
    mudanca = input(f"Digite a sua Alteração: ")
    Oq_mudar = input(f"Digite o código do livro que deseja alterar: ")
    
    if escolha == 1:
        opcao = 'codigo'
    elif escolha == 2:
        opcao = 'nome'
    elif escolha == 3: 
        opcao = 'quantidade'
    else:
        print("Opção inválida tente novamente")
        atualizar_livro() 
        
    cursor.execute(f"update livro set {opcao} = ? where codigo = ?",(mudanca, Oq_mudar))
    cursor.commit()  
    
    ver_livros()

def deletar_livro():
    
    ver_livros()
    
    ra = input("Digite o código do livro que deseja deletar: ")
    
    cursor.execute(f" delete from livro where codigo = {ra}")
    cursor.commit()
    
    ver_livros()