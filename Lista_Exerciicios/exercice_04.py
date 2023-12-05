def find_element(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        raise IndexError("Índice inválido. Fora dos limites da lista.")
