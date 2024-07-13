import integracao_sql
import pandas as pd
from datetime import datetime, timedelta


integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def ver_historico():
    
    tabela = pd.read_sql(f'select * from historico',conexao)  
    print(tabela)
    
def inserir_historico(datetime,ra,codigo_livro,estado,continuar):
    
    print(f"pressione enter para continuar \npara sair digite '!n'")
    continuar = ""
    
    
    while continuar != "!n":
        continuar = input('Deseja continuar: ')
        
        if continuar != "!n":
            
            data_retirada = datetime.today()
            data_retirada_formatada = data_retirada.strftime("%d/%m/%y")
                        
            data_devolucao = data_retirada + timedelta(days=30)
            data_devolucao_formatada = data_devolucao.strftime("%d/%m/%y")
            
            if estado != 'pendente' or estado != 'entregue':
                print("Opção inválida tente novamente")
                inserir_historico(datetime)

            cursor.execute(f"insert into historico(RA_aluno,codigo_livro,dataRetirada,dataDevolucao,estado) values (?,?,?,?,?)",(ra,codigo_livro,data_retirada_formatada,data_devolucao_formatada,estado))
            cursor.commit()    
    
        ver_historico()
        
def Atualizar_historico(escolha,mudanca,Oq_mudar,opcao):
    
    ver_historico()
    
    print("Digite o número da opção que deseja alterar")
    print(f"1) Ra do aluno\n 2) Código do livro\n 3) estado")
    
    opcao = ''
    
    if escolha == 1:
        opcao = 'RA_aluno'
    elif escolha == 2:
        opcao = 'codigo_livro'
    elif escolha == 3: 
        opcao = 'estado'
    else:
        print("Opção inválida tente novamente")
        Atualizar_historico() 
        
    cursor.execute(f"update historico set {opcao} = ? where codigo = ?",(mudanca, Oq_mudar))
    cursor.commit()  
    
    ver_historico()

def deletar_historico(ra):
    
    ver_historico()
    
    cursor.execute(f" delete from historico where codigo = {ra}")
    cursor.commit()
    
    ver_historico()
