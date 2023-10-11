import os

class CantBeZero(BaseException):
    pass


def division(val1, val2):
    try:
        return val1 / val2
    except ZeroDivisionError:
        print('[Error] Você não pode dividir um número por zero!')
    except BaseException as error:
        print(f'[Error] Ocorreu um erro: {error}')


def input_int(message, canBeZero=True):
    try:
        value = int(input(message))
        if not canBeZero and value == 0:
            raise ValueError("[Error] Não é possível inserir zero!")
        return value
    except CantBeZero:
        print("[Error] O número inserido não é válido!")
    except BaseException as error:
        print("[Error] Oops, ocorreu um erro!")


def main():
    while True:
        try:
            number_one = input_int('Digite o primeiro valor:')
            number_two = input_int('Digite o segundo valor:', canBeZero=False)
    
            result = division(number_one, number_two)
            print(f'Resultado: {result}')
        except ValueError as error:
            print(f"Unexpected {error=}")
        except BaseException as error:
            print(f"Unexpected {error=}")
        else:
            print('(-_-) Ok')
        finally:
           input("Pressione qualquer tecla para continuar:")
           print('Vá embora(*_*)')

main()
