import pandas as pd

dados = pd.read_csv("dados.csv")
dados = dados.drop('is_business_travel_ready', axis=1)
colunas = list(dados.columns)[1:-1]
print(colunas)