def avaliar_produto():
    try:
        nota = int(input("Digite uma nota de 0 a 10: "))
        assert 0 <= nota <= 10, "Nota fora do intervalo permitido (0 a 10)."
        print(f"A nota {nota} é válida.")
    except ValueError:
        print("Por favor, digite um número inteiro.")
    except AssertionError as e:
        print(f"Erro: {e}")
