def verificar(matriz):
    tamanho = len(matriz)
    
    for i in range(tamanho):
        for j in range(tamanho):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True 


matriz_simetrica = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

matriz_nao_simetrica = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]

print(verificar(matriz_simetrica)) 
print(verificar(matriz_nao_simetrica))
