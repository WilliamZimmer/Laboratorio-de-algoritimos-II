### Codigo para analizar e manipular números pares dentro do array com menu.

array = []

while True:
    print("Menu:")
    print("1 - Inserir item")
    print("2 - Listar itens")
    print("3 - Retirar item")
    print("4 - Retirar todos os itens")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        item = int(input("Digite um número par para inserir: "))
        if item % 2 != 0:
            print("Erro: O número inserido não é par.")
            continue
        array.append(item)
        print("Item inserido com sucesso!")
    
    elif opcao == 2:
        if len(array) == 0:
            print("O array está vazio.")
        else:
            print("Itens do array:")
            for item in array:
                print(item)
    
    elif opcao == 3:
        if len(array) == 0:
            print("O array está vazio.")
        else:
            item = int(input("Digite o número par que deseja retirar: "))
            if item % 2 != 0:
                print("Erro: O número inserido não é par.")
                continue
            if item in array:
                array.remove(item)
                print("Item removido com sucesso!")
            else:
                print("O número informado não está presente no array.")
    
    elif opcao == 4:
        if len(array) == 0:
            print("O array já está vazio.")
        else:
            array.clear()
            print("Itens removidos.")
    
    elif opcao == 5:
        print("Saindo do programa!")
        break
    
    else:
        print("Opção inválida.")
    
    print()
