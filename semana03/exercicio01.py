import random

def validate_number(matriz, number):
    for line in range(len(matriz)): 
        for column in range(len(matriz[line])):
            if matriz[line][column] == number:
                return False

    return True

def generate_bingo():
    matriz = []

    for line in range(5):
        matriz.append([])

        for column in range(5):
            random_number = random.randint(0, 99)
            while not validate_number(matriz, random_number):
                random_number = random.randint(0, 99)
            matriz[line].append(random_number)
            
    return matriz

def main():
    matriz = generate_bingo()
    print("Cartela gerada:")
    for line in matriz:
        print(line)

main()
