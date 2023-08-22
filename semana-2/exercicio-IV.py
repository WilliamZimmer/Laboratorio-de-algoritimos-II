def calcular_media(lista):
    soma = 0
    for valor in lista:
        soma += valor
    return soma / len(lista)

def calcular_valores_medios(matriz):
    valores_mediosL = []
    
    total = 0
    elementos = 0
    
    for linha in matriz:
        soma_linha = 0
        for valor in linha:
            soma_linha += valor
            total += valor
            elementos += 1
        valor_linha = soma_linha / len(linha)
        valores_mediosL.append(valor_linha)
    
    valor_medio = total / elementos
    return valor_medio, valores_mediosL


matriz = [
    [9, 10, 12],
    [8, 8, 1],
    [1, 15, 4]
]

valor_medio, valores_mediosL = calcular_valores_medios(matriz)
print("Valor médio total da matriz:", valor_medio)
print("Valores médios por linha:", valores_mediosL)
