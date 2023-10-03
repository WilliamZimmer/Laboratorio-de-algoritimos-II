def calcular(valor):
    notas_disponiveis = [100, 50, 20, 10]
    resultado = []

    for nota in notas_disponiveis:
        while valor >= nota:
            resultado.append(nota)
            valor -= nota

    return resultado

def main():
    saque = int(input("Digite o valor: R$ "))
    notas_entregues = calcular(saque)

    if len(notas_entregues) == 0:
        print("Não é possível efetuar o saque.")
    else:
        print("Entregar as seguintes notas:")
        for nota in notas_entregues:
            print("R$", nota)

main()


