def generate():
    cartela = []
    numero = 0

    while len(cartela) < 25:
        cartela.append(numero)
        numero += 1

        if numero > 99:
            numero = 0

    return cartela

def exibir_cartela(cartela):
    for i in range(5):
        linha = cartela[i * 5:(i + 1) * 5]
        print(linha)

cartela = generate()
exibir_cartela(cartela)

