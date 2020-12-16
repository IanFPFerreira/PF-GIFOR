# Dado um arquivo csv com delimitador ';' e com o seguinte cabeçalho:
# id;nome;telefone;idade.
# Retorne uma lista com os registro ordenados por nome.
# Exemplo de arquivo:
# Id;nome;telefone;idade
# 1;João;43383832;28
# 2;Maria;43839322;32
# .
# .
# .
# N;Zzzz;99999999;12


# Importando a bilbioteca para trablhar com arquivos csv's
import csv

# Função que defini qual arquivo será utilizado
with open('dados.csv') as dados_csv:

    # Difinindo a variável que terá como valor o arquivo csv
    dados = csv.reader(dados_csv, delimiter=';')

    # Método que pula a primeira linha do csv, no caso, o cabeçalho
    dados.__next__()

    # Definindo uma lista
    lista_de_dados = []

    # Estrutura de repetição que passará por cada linha do arquivo csv e
    # adicionará na 'lista_de_dados' toda a linha no formato de lista, logo,
    # a 'lista_de_dados' será uma lista de listas
    for linha in dados:
        lista_de_dados.append(linha)

    # Ordenando a 'lista_de_dados' pelo índice '1' (que representa o nome) de
    # cada lista que está contida na 'lista_de_dados'
    lista_de_dados_ordenada = sorted(lista_de_dados, key=lambda x: x[1])

    # Estrutura de repetição que passará por cada lista dentro da
    # 'lista_de_dados_ordenada', e imprimirá na tela cada lista
    for lista in lista_de_dados_ordenada:
        print(lista)
