class InvalidMonthError(BaseException):
    pass

def month_word(month):
    try:
        units = ("Janeiro!", "Fevereiro!", "Março!", "Abril!", "Maio!", "Junho!", "Julho!", "Agosto!", "Setembro!", "Outubro!", "Novembro!", "Dezembro!")
        if month >= 1 and month <= 12:
            return units[month -1] 
        else:
            raise InvalidMonthError
            
    except InvalidMonthError as error:
        print(error)
    except BaseException as error:
        print("[Error] Oops, ocorreu um erro inesperado:", error)        
            

def main():
    while True:
        try:
            month = int(input("Digite um mês: "))
            word = month_word(month)
            print("O mês:", month, "por extenso é: ", word)
        except ValueError:
            print("[Error] Mês inválido")
        except InvalidMonthError:
            print("[Error] Mês inválido. O mês deve estar entre 1 e 12.")

main()
