import pandas as pd

tabela_vendas = pd.read_excel('Vendas.xlsx')


pd.set_option('display.max_columns', None)
print(tabela_vendas)
