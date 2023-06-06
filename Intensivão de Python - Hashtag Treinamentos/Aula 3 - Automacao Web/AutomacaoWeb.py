#   Passo 0:    Baixar e/ou importar os pacotes
#   baixar o chromedriver e colocar o arquivo dentro da pasta do python.exe
from selenium import webdriver as wd        # pip install selenium
import pandas as pd                         # pip install pandas
import unicodedata

#   Passo 1:    Abrir o navegador
navegador = wd.Chrome()

#   Passo 2:    Importar a base de dados
tabela = pd.read_excel('commodities.xlsx')
#   Passo 2.1:   Entrar no site melhor cambio
navegador.get('https://www.melhorcambio.com/milho-hoje')
#   Passo 2.2:   Pegar o preço da cotação do milho
cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
# navegador.find_element().send_keys('meu nome é Caique') = escrever nele
# navegador.find_element().click() = clica nele
# navegador.find_element().get_attribute() = pegar uma informação dele
cotacao = cotacao.replace('.', '').replace(',', '.')
cotacao = float(cotacao)
#   Passo 2.3:   Na coluna Preço Atual, preencher a cotação do milho
tabela.loc[0, 'Preço Atual'] = cotacao

#   Passo 3:    Para cada produto da base
for linha in tabela.index:
    produto = tabela.loc[linha, 'Produto']
    link = f'https://www.melhorcambio.com/{produto}-hoje'
    link = link.replace('á', 'a').replace('ã', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ç', 'c')
#    link = unicodedata.normalize('NFKD', link).encode('ascii', 'ignore')
    navegador.get(link)
    cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    cotacao = cotacao.replace('.', '').replace(',', '.')
    cotacao = float(cotacao)
    tabela.loc[linha, 'Preço Atual'] = cotacao
    print(f'Informações do produto {produto} coletada com sucesso!')

#   Passo 4:    Quais produtos serão comprados
tabela['Comprar'] = tabela['Preço Atual'] < tabela['Preço Ideal']
navegador.quit()
print('Informações coletadas com sucesso!')

#   Passo 5:    Exportar a base de dados atualizada
tabela.to_excel('commodities_atualizada.xlsx', index=False)

print(tabela)
print('Planilha atualizada com sucesso!')
