import integracao_sql
import pandas as pd

cursor, conexao = integracao_sql.juncao_sql()

def ver_livros():
    
    tabela = pd.read_sql(f'select * from livro',conexao)  
    print(tabela)
  
def inserir_livros(codigo_livro,nome_livro,quantidade,continuar):
    
    print(f"pressione enter para continuar \npara sair digite '!n'")
    continuar = ""
    
    while continuar != "!n":
        continuar = input('Deseja continuar: ')
        
        if continuar != "!n":
            cursor.execute(f"insert into livro(codigo,nome,quantidade) values ({codigo_livro},'{nome_livro}',{quantidade})")
            cursor.commit()  
            
        else:   
            ver_livros()

def atualizar_livro(escolha,mudanca,Oq_mudar,opcao):
    
    ver_livros()
    
    print("Digite o número da opção que deseja alterar")
    print(f"1) Código do livro\n 2) Nome do livro\n 3) Quantidade de livro")
    
    opcao = ''
    
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

def deletar_livro(codigo_livro):
    
    ver_livros()
    
    cursor.execute(f" delete from livro where codigo = {codigo_livro}")
    cursor.commit()
    
    ver_livros()