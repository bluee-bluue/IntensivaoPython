# Passo 0: Instalar os pacotes: PYAUTOGUI, PANDAS, OPENPYXL, NUMPY
# pip install pyautogui
# pip install pandas
# pip install openpyxl
# pip install numpy
import sys

# Passo 0.1: importar os pacotes
import pyautogui as pyg
import time
import pandas
import pyperclip as pyc

# pyautogui.click -> clica com o mouse (click=2 após a localização é igual a duplo clique)
# pyautogui.write -> escrever um texto
# pyautogui.press -> aperta um tecla
# pyautogui.hotkey -> apertar uma combinação de teclas
# pyautogui.PAUSE = x ou time.sleep(x) -> pausa para o proximo comando
# print(pyautogui.position()) -> mostra a posição do mouse
# pyautogui.scroll -> usa o scroll do mouse
# pyautogui.dragTo -> arrasta o mouse

pyg.PAUSE = 1
# Passo 1: Acessar o sistema da empresa
pyg.press('win')
time.sleep(1)
pyg.click(x=904, y=159)
pyg.write('chrome')
time.sleep(1)
pyg.press('enter')
time.sleep(1)
pyg.click(x=621, y=623)
time.sleep(2)
pyg.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyg.press('enter')
time.sleep(2)

# Passo 2: Fazer login no sistema
pyg.click(x=939, y=478)
pyg.write('meu login')
pyg.click(x=939, y=578)
pyg.write('minha senha')
pyg.click(x=939, y=678)
time.sleep(2)

# Passo 3: Baixar a base de dados
pyg.click(x=471, y=558)
pyg.click(x=628, y=253)
time.sleep(4)

# Passo 4: Importar a base de dado
# s
tabela = pandas.read_csv(r'C:\Users\scaiq\Downloads\Compras.csv', sep=';')
print(tabela)

# Passo 5: Calcular os indicadores
total_gasto = tabela['ValorFinal'].sum()
quantidade = tabela['ValorUnitário'].sum()
preco_medio = (total_gasto + quantidade) / 2

total_gasto = f'R${total_gasto:_.2f}'
total_gasto = total_gasto.replace('.', ',').replace('_', '.')
print(total_gasto)

quantidade = f'R${quantidade:_.2f}'
quantidade = quantidade.replace('.', ',').replace('_', '.')
print(quantidade)

preco_medio = f'R${preco_medio:_.2f}'
preco_medio = preco_medio.replace('.', ',').replace('_', '.')
print(preco_medio)

# Passo 6: Enviar o email para a diretoria/para o chefe
texto_google = 'https://www.google.com/webhp?authuser=1'
pyc.copy(texto_google)
pyg.hotkey('ctrl', 't')
pyg.hotkey('ctrl', 'v')
pyg.press('enter')
time.sleep(2.5)
pyg.click(x=1666, y=167)
time.sleep(5)
pyg.click(x=94, y=250)
time.sleep(2)
pyg.write('pythonimpressionador@gmail.com')
pyg.press('tab')
pyg.press('tab')
texto_assunto = 'Relatório de Compras'
pyc.copy(texto_assunto)
pyg.hotkey('ctrl', 'v')
pyg.press('tab')
texto_conteudo = f'''
Prezados,
Segue o relatório de compras

Total gasto: {total_gasto})
Quantidade de Produtos: {quantidade})
Preço Médio: {preco_medio})

Qualquer dúvida entrar em contato.

Att.,
Caique
'''
pyc.copy(texto_conteudo)
pyg.hotkey('ctrl', 'v')
