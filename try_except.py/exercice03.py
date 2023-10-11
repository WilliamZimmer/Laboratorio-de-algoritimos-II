def define(n):
    try:
        if n % 4 == 0 and n % 100 != 0:
            print("O ano: ", n, "é bissexto!")
        elif n % 400 == 0:
            print("O ano: ", n, "é bissexto!")
        else:
            print("o ano: ", n, "não é bissexto!")
            
    except ValueError as error:
        print(f"Unexpected {error=}")
    except BaseException as error:
        print(f"Unexpected {error=}")
    else:
        print('(-_-) Ok')
    finally:
        input("Pressione qualquer tecla para continuar:")
        print('Vá embora(*_*)')
           
def main():
    while True:
        n = int(input('Digite um ano: '))
        define(n)    
    
main()
