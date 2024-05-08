import pandas as pd

url = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
dados = pd.read_csv(url)

if 32 in dados["movieId"].values:
    filme_id_32 = dados[dados["movieId"] == 32]

    if filme_id_32["rating"].values[0] > 3:
        print("Filme ID:", filme_id_32["movieId"].values[0])
        print("É um filme bom.")
    else:
        print("Filme ID:", filme_id_32["movieId"].values[0])
        print("Não é um filme bom.")
else:
    print("O filme com ID=32 não foi encontrado.")
