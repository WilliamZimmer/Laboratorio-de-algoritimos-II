def x(matriz):
    soma = 0
    n = len(matriz)

    for i in range(n):
        for j in range(i):
            soma += matriz[i][j]

    return soma

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = x(matriz)
print("A soma dos elementos é:", result)
