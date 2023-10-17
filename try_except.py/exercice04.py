import math

def calculate_imports(N, M):
    if M < 0 or M > N:
        return 0 

    combination = math.factorial(N) / (math.factorial(M) * math.factorial(N - M))
    return combination

N = int(input("Digite o número total de alunos (N): "))
M = int(input(f"Digite o número de alunos em um dos grupos (-M-, deve ser menor que {N}): "))

combination = calculate_imports(N, M)
print(f"O número de combinações possíveis é: {int(combination)}")
