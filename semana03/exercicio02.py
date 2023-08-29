def calcular_diagonal_inferior(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            soma += matriz[i][j]
    return soma


matriz = [
    [1, 2, 3],
    [5, 6, 7],
    [9, 10, 11],

]

soma_diagonal_inferior = calcular_diagonal_inferior(matriz)
print("Matriz:")
for linha in matriz:
    print(linha)
print("Soma abaixo da diagonal principal:", soma_diagonal_inferior)
