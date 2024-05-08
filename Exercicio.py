import pandas as pd

url = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
dados = pd.read_csv(url)

print("Primeiros 12 registros:")
print(dados.head(12))

print("\nÚltimos 6 registros:")
print(dados.tail(6))

print("\nTamanho da massa de dados:")
print(dados.shape)
