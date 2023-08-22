def somar(matriz1, matriz2):
    matriz = []
    
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = matriz1[i][j] + matriz2[i][j]
            linha.append(elemento)
        matriz.append(linha)
    
    return matriz

matriz1 = [
    [4, 0, 30],
    [-21, 5, 6],
    [7, 15, 6]
]

matriz2 = [
    [9, -3, -6],
    [1, 48, 1],
    [3, 2, 8]
]

resultante = somar(matriz1, matriz2)
for linha in resultante:
    print(linha)
