def maior_sequencia(matriz):
    n = len(matriz)
    maior = 0

    for i in range(n):
        for j in range(n - 4):
            horizontal = vertical = 1
            for k in range(5):
                horizontal *= matriz[i][j + k]
                vertical *= matriz[j + k][i]
            maior = max(maior, horizontal, vertical)


    for i in range(n - 4):
        for j in range(n - 4):
            diagonal = 1
            for k in range(5):
                diagonal *= matriz[i + k][j + k]
            maior = max(maior, diagonal)

    return maior

matriz = [
    [2, 1, 1, 1, 1],
    [1, 2, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 2, 1],
    [1, 1, 1, 1, 2]
]

resultado = maior_sequencia(matriz)
print("Maior produto de 5 números consecutivos:", resultado)
