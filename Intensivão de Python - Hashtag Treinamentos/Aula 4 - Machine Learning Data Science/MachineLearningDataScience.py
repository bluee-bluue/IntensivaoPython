#   Passo 0:    Baixar e/ou importar os pacotes
import pandas as pd
import seaborn as sns  # pip install seaborn
import matplotlib.pyplot as plt  # pip install matplotlib
from sklearn.model_selection import train_test_split  # pip install scikit-learn
from sklearn.linear_model import LinearRegression     # modelo_regressao_linear = LinearRegression()
from sklearn.ensemble import RandomForestRegressor    # modelo_arvore_decisao = RandomForestRegressor()
from sklearn.metrics import r2_score

#   Passo 1:    Extração/Obtenção de dados
tabela = pd.read_csv('barcos_ref.csv')

#   Passo 2:    Ajustes de dados, tratamento/limpeza da tabela (nesse caso não foi preciso)

#   Passo 3:    Análise exploratória
# print(tabela.corr()[['Preco']])
#   Passo 3.1:     Cria o grafico
sns.heatmap(tabela.corr()[['Preco']], cmap='Blues', annot=True)
#   Passo 3.2:     Exibe o grafico
plt.show()

#   Passo 4:    Modelagem + Algoritmos (Inteligência Artificial, se necessário)
#   Passo 4.1:     Preparação: separar a base em dados de X e Y
y = tabela['Preco']
x = tabela.drop('Preco', axis=1)  # axis 0 = linhas, axis 1 = colunas

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)
#   Passo 4.2:  Importar, criar e treinar a IA
#   já importado
#   Passo 4.2.1:   Criar a IA
modelo_regressao_linear = LinearRegression()
modelo_arvore_decisao = RandomForestRegressor()
#   Passo 4.2.2:   Treinar a IA
modelo_regressao_linear.fit(x_treino, y_treino)
modelo_arvore_decisao.fit(x_treino, y_treino)

previsao_regressao_linear = modelo_regressao_linear.predict(x_teste)
previsao_arvore_decisao = modelo_arvore_decisao.predict(x_teste)

#   Passo 5:    Interpretação de resultados
print(r2_score(y_teste, previsao_regressao_linear))
print(r2_score(y_teste, previsao_arvore_decisao))

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar['Previsões Arvore Decisões'] = previsao_arvore_decisao
tabela_auxiliar['Previsões Regressão Linear'] = previsao_regressao_linear
sns.lineplot(data=tabela_auxiliar)
plt.show()

tabela_nova = pd.read_csv('novos_barcos.csv')
print(tabela_nova)
previsao = modelo_arvore_decisao.predict(tabela_nova)
print(previsao)
