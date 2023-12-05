class NegativeNumberError(Exception):
    def __init__(self, message="A raiz quadrada de números negativos não é real."):
        self.message = message
        super().__init__(self.message)

def calculate_square_root(numero):
    if numero < 0:
        raise NegativeNumberError()
    return numero ** (1/2)
