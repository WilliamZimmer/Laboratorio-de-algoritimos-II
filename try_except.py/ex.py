while True:
    try:
        x = int(input("Digite um número inteiro:"))
        n = int(input("Digite um número inteiro:"))
        d = x/n
        print(d)
    except ValueError as err:
        print(f"Unexpected {err=}")
    except NameError as err:
        print(f"Unexpected {err=}")
    else:
        if x and n >= 0:
            print("Tudo certo!")
        if x and n 
        else:
            print("Números negativos são inválidos!")
        break  
    finally:
        print("Goodbye!")
