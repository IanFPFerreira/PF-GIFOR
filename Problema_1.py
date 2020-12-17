# Dado uma lista de dicionários (chave/valor) Python, verifique se existe a
# chave 'nome', e caso exista, salve o valor dessa chave em uma segunda lista,
# de modo que não haja repetição de valores na segunda lista.

# Criando uma lista de dicionarios
lista_dicionario = [
    {'nome': 'Maria', 'idade': 20},
    {'nome': 'João', 'idade': 30},
    {'nome': 'Ítalo', 'idade': 40},
    {'nome': 'Guilherme', 'idade': 50},
    {'idade': 25},
    {'nome': 'Gabriel', 'idade': 35},
    {'nome': 'Maria', 'idade': 45},
    {'idade': 55},
    {'nome': 'Guilherme', 'idade': 50},
    {'nome': 'Álvaro', 'idade': 65},
    {'nome': 'Gabriel', 'idade': 35},
]

# Criando uma lista vazia que conterá o valor da chave 'nome'
lista_valores = []

# Estrutura de repetição que passará por cada dicionário dentro da lista
for dicionario in lista_dicionario:

    # Estrutura condicional que verifica se o dicionário possui a chave
    # 'nome', se a condição for verdadeira o valor da chave 'nome' é
    # adicionado à 'lista_valores'
    if 'nome' in dicionario:
        lista_valores.append(dicionario.get('nome'))


# A 'lista_valores' é convertida para um conjunto e convertida novamente para
# uma lista, deste modo é retirado os valores repetidos, já que em conjuntos
# não pode haver repetição de elementos
lista_valores = list(set(lista_valores))

# Imprimi na tela uma lista contendo os valores da chave 'nome'
print(lista_valores)
