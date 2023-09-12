
def menu():
    print("\n --------OPÇÕES--------")
    print("1. Adicionar um produto")
    print("2. Buscar um produto")
    print("3. Visualizar todos os produtos")
    print("4. Vender um produto")
    print("5. Relatório de Vendas")
    print("6. Sair")

    option =  int(input("\n Digite sua opção de escolha: "))

    return option

def add_product(stock):
    name = input("Digite o nome do produto a ser ADICIONADO: ")
    quant = int(input("Digite a quantidade do produto a ser adicionado: "))
    price = float(input("Digite o preço unitário: "))

    if name in stock:
        stock[name]['Quant'] += quant
    else:
        stock[name] = {'Quant': quant, 'Price': price}


def search_product(stock):
    name = input("Digite o nome do produto a ser PROCURADO: ")

    if name in stock:
        print("------------------------------------------------")
        print(f"Produto: {name}")
        print(f"Quantidade em estoque: {stock[name]['Quant']}")
        print(f"Preço unitário: R${stock[name]['Price']}")
    else:
        print("\t \n Produto não foi encontrado no estoque!")

def view_products(stock):
    print("\n -----> Produtos disponíveis:")
    for name, info_products in stock.items():
        print(f"Produto: {name}")
        print(f"Quantidade em estoque: {info_products['Quant']}")
        print(f"Preço unitário: R${info_products['Price']}")
        print("------------------------------------------------")


def sell_product(stock, sales_extract):
    name = input("Digite o nome do produto vendido: ")
    sold_quant = int(input("Digite a quantidade vendida: "))

    if name in stock and stock[name]['Quant'] >= sold_quant:
        sale_value = sold_quant * stock[name]['Price']
        stock[name]['Quant'] -= sold_quant
        print("-------- VENDA --------")
        print(f"Produto vendido: {name}")
        print(f"Quantidade vendida: {sold_quant}")
        print(f"Valor total da venda: R${sale_value:.2f}")
    else:
        print("Produto não encontrado no estoque ou quantidade insuficiente em estoque!")

    sales_extract[name] = {'Quant': sold_quant, 'Price': sale_value}


def sales_report(sales_extract):
    print("\n -----> Relatório de Vendas:")
    for name, info_products in sales_extract.items():
        print(f"Produto: {name}")
        print(f"Quantidade vendida: {info_products['Quant']}")
        print(f"Valor total da venda: R${info_products['Price']}")
        print("------------------------------------------------")
    

def main():
    stock = {}
    sales_extract = {}
    while True:
        option = menu()

        if option == 1:
            add_product(stock)

        elif option == 2:
            search_product(stock)

        elif option == 3:
            view_products(stock)

        elif option == 4:
            sell_product(stock, sales_extract)

        elif option == 5:
            sales_report(sales_extract)

        elif option == 6:
            print('Estoque:', stock)
            break

main()
