conta_bancaria = {
    "saldo": 0,
    "depositos": 0,
    "saques": 0,
    "historico": [],
    "transaction_limit": 1000
}

def deposit(valor):
    if valor > 0:
        conta_bancaria["saldo"] += valor
        conta_bancaria["depositos"] += 1
        conta_bancaria["historico"].append(f"Depósito de R$ {valor:.2f}")

def withdraw (valor):
    if valor > 0 and valor <= conta_bancaria["saldo"] and valor <= conta_bancaria["transaction_limit"]:
        conta_bancaria["saldo"] -= valor
        conta_bancaria["saques"] += 1
        conta_bancaria["historico"].append(f"Saque de R$ {valor:.2f}")

def check():
    return conta_bancaria["saldo"]

def movement():
    return conta_bancaria["historico"]

while True:
    print("Opções:")
    print("1. Depositar dinheiro")
    print("2. Sacar dinheiro")
    print("3. Verificar saldo bancário")
    print("4. Histórico de movimentações")
    print("5. Sair")
    choice = input("Digite sua opção de escolha: ")

    if choice == "1":
        try:
            valor = float(input("Digite o valor a ser depositado: "))
            deposit(valor)
            print("Depósito realizado com sucesso.")
        except ValueError:
            print("Valor inválido. Por favor, insira um valor numérico válido.")
    elif choice == "2":
        try:
            valor = float(input("Digite o valor a ser sacado: "))
            withdraw(valor)
            print("Saque realizado com sucesso.")
        except ValueError:
            print("Valor inválido. Por favor, insira um valor numérico válido.")
    elif choice == "3":
        saldo = check()
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif choice == "4":
        movimentacoes = movement()
        for movimentacao in movimentacoes:
            print(movimentacao)
        print(f"Quantidade de depósitos: {conta_bancaria['depositos']}")
        print(f"Quantidade de saques: {conta_bancaria['saques']}")
    elif choice == "5":
        print("Saindo do sistema. Obrigado!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
