#   Passo 0:    Baixar e/ou importar os pacotes
import pandas                   # pip install pandas
import plotly.express as px     # pip install plotly

#   Passo 1:    Importar a base de dados
#   Passo 1.1:  Deletar colunas inuteis
#   axis 0 = deletar linha; axis 1 = deletar coluna
tabela = pandas.read_csv('clientes.csv', encoding='latin', sep=';')


#   Passo 2:    Visualizar a base de dados
#   Passo 2.1:  Entender as informações que você tem disponíveis
#   Passo 2.2:  Procurar as cagadas da base de dados
tabela = tabela.drop('Unnamed: 8', axis=1)
print(tabela)

#   Passo 3:    Tratamento de dados
#   Passo 3.1:  Valores no formato errado - convertendo os valores em texto para numerico
tabela['Salário Anual (R$)'] = pandas.to_numeric(tabela['Salário Anual (R$)'], errors='coerce')
#   Passo 3.2:  Valores vazios
tabela = tabela.dropna()  # apagando linhas vazias
print(tabela.info())  # para visualizar as informações da tabela

#   Passo 4:    Análise inicial = entender como estão as notas dos clientes
print(tabela.describe())

#   Passo 5:    Análise comleta = traçar o perfil ideal de cliente = entender como cada característica do cliente importa na nota
#   Passo 5.1:  Cria o gráfico
#   x e y = colunas; text_auto=True = mostrar texto; nbins=10 = maximo de colunas; histfunc='avg' = media; color=nomeDaTabela = muda a cor para comparações
#   colunaX = 'Profissão'
#   colunaY = 'Nota (1-100)'
#   grafico = px.histogram(tabela, x=colunaX, y=colunaY, histfunc='avg', text_auto=True, nbins=10)
for coluna in tabela.columns:
    if coluna != 'Nota (1-100)':
        grafico = px.histogram(tabela, x=coluna, y='Nota (1-100)', histfunc='avg', text_auto=True, nbins=10)
        #   Passo 5.2:  Exibe o gráfico
        grafico.show()

#   Perfil ideal de cliente:
#   Clientes acima de 15 anos
#   Áreas de trabalho: Entretenimento e Artista (evitar Contrução)
#   Experiência de trabalho: Ter entre 10 e 15 anos de experiência
#   Família de até 7 pessoas
#   Obs final: O salário não parece fazer muita diferença. Clientes de promoção paracem ter uma leve nota menor, mas não tanto
