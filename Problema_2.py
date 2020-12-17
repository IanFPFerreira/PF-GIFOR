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

# Definindo uma variável do tipo string que possuirá todos os possíveis tipos
# de acentuações
com_acento = 'aáàãâAÂÁÀÃbBcCçÇdDeéEÉfFgGğĞhHiİîÎíīıIÍjJkKlLmMnNóoõOöÖÓpPqQrRsSşŞtTuUûúÛüÜÚvVwWxXyYzZ'

# Definindo uma variável do tipo string que possuirá todos os caracteres sem
# acentuações
sem_acento = 'aaaaaAAAAAbBcCcCdDeeEEfFgGgGhHiIiIiiiIIjJkKlLmMnNoooOoOOpPqQrRsSsStTuUuuUuUUvVwWxXyYzZ'

# Função built-in do Python que faz o mapeamento de uma string e troca todos
# os caracteres da variável 'com_acento' pelo seu correspondente na variável
# 'sem_acento'
mapear = str.maketrans(com_acento, sem_acento)


def transforma(nome):
    """
    Função que recebe uma lista e retorna o valor no index 1 que é tranfomado
    pela função que retira os caracteres especiais, o index 1 corresponde ao
    nome no arquivo csv
    """
    return nome[1].translate(mapear)


# Função que defini qual arquivo será utilizado, passando também o parâmetro
# "encoding='utf-8'", que permite receber um arquivo com caracteres especiais
with open('dados.csv', encoding='utf-8') as dados_csv:

    # Definindo a variável que terá como valor o arquivo csv
    dados = csv.reader(dados_csv, delimiter=';')

    # Método que pula a primeira linha do csv, no caso, o cabeçalho
    dados.__next__()

    # Definindo uma lista vazia que possuirá cada linha do arquivo csv
    lista_de_dados = []

    # Estrutura de repetição que passará por cada linha do arquivo csv
    for linha in dados:
        # Adicionará na 'lista_de_dados' toda a linha no formato de lista,
        # logo, a 'lista_de_dados' será uma lista de listas
        lista_de_dados.append(linha)

    # Definindo uma lista vazia que conterá os nomes sem acentos
    lista_de_nomes = []

    # Estrutura de repetição que passará por cada lista dentro da
    # 'lista_de_dados'
    for lista in lista_de_dados:
        # Cada lista entrará na função 'transforma', o que irá retornar o
        # nome sem caracteres especiais
        nome = transforma(lista)
        # Cada nome será adicionado na 'lista_de_nomes'
        lista_de_nomes.append(nome)

    # Estrutura de repetição que passará por cada lista dentro da
    # 'lista_de_dados'
    for i in range(len(lista_de_nomes)):
        # Cada lista na 'lista_de_dados' terá o valor do index 1, que
        # corresponde ao nome, trocado pelo nome contido na 'lista_de_nomes',
        # nome este que já está sem caracteres especiais
        lista_de_dados[i][1] = lista_de_nomes[i]

    # Ordenando a 'lista_de_dados' pelo índice '1' (que representa o nome) de
    # cada lista que está contida na 'lista_de_dados'. A decisão de se retirar
    # os acentos dos nomes foi para se fazer uma melhor ordenação
    lista_de_dados_ordenada = sorted(lista_de_dados, key=lambda x: x[1])

    # Estrutura de repetição que passará por cada lista dentro da
    # 'lista_de_dados_ordenada', e imprimirá na tela cada lista
    for lista in lista_de_dados_ordenada:
        print(lista)
