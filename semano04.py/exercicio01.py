def colect_info():
    person = {}

    person['name'] = input("Digite o nome:")
    person['age'] = input("Digite a idade:")
    person['sex'] = input("Digite o sexo:")
    person['city'] = input("Digite a cidade:")
    person['estate'] = input("Digite o estado:")

    return person

def main():
    info = colect_info()

    print("Informações coletadas:")
    print("Nome: ", info["name"])
    print("Idade: ", info["age"])
    print("Sexo: ", info["sex"])
    print("Cidade: ", info["city"])
    print("Estado: ", info["estate"])

main()
