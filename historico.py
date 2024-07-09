import integracao_sql
import pandas as pd
from datetime import datetime, timedelta


integracao_sql.juncao_sql()

cursor, conexao = integracao_sql.juncao_sql()

def ver_historico():
    
    tabela = pd.read_sql(f'select * from historico',conexao)  
    print(tabela)
    
def inserir_historico(datetime):
    
    print(f"pressione enter para continuar \npara sair digite '!n'")
    dados = ""
    
    
    while dados != "!n":
        dados = input('Deseja continuar: ')
        
        if dados != "!n":
            
            ra = input("Digite o RA do aluno: ")
            codigo_livro = int(input(f'Digite o código do livro: '))
            estado = input(f"Digite o status de entrega (pendente/entregue): ").lower()
            
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