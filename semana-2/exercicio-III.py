def encontrar_valor(linha):
    maior = linha[0]
    for valor in linha:
        if valor > maior:
            maior = valor
    return maior
  
def somar(matriz):
    somas = []
    for linha in matriz:
        maior_valor = encontrar_valor(linha)
        somas.append(maior_valor)
    return somas
  
matriz = [
    [5, 10, 3],
    [8, 2, 7],
    [1, 6, 4]
]

somas = somar(matriz)
print(somas) 
