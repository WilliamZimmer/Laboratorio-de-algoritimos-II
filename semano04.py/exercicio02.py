buy_list = {}

while True:
    print("\nOpções:")
    print("1. Adicionar à lista")
    print("2. Verificar na lista")
    print("3. Exibir compras")
    print("4. Exit")

    choice = input("Digite sua escolha: ")

    if choice == "1":
        product_name = input("Qual o nome do produto: ")
        quantity = int(input("Qual a quantidade: "))
        
        if product_name in buy_list:
            buy_list[product_name] += quantity
        else:
            buy_list[product_name] = quantity
        
        print(f"{quantity} {product_name} adicionado à lista.")

    elif choice == "2":
        product_name = input("Digite o nome do produto: ")
        if product_name in buy_list:
            print(f"{product_name} está na lista com {buy_list[product_name]} unidades.")
        else:
            print(f"{product_name} não está na lista.")

    elif choice == "3":
        print("Lista de Compras:")
        for product, quantity in buy_list.items():
            print(f"{product}: {quantity}")

    elif choice == "4":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Escolha uma opção válida.")
