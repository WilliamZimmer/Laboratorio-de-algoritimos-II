#Crie um método para verificar se um triângulo é equilátero (todos os lados iguais),
#isósceles (dois lados iguais) ou escaleno (todos lados diferentes). Se os lados não
#formarem um triângulo válido (se a soma de dois lados for menor que o terceiro lado),
#lance uma exceção ValueError utilizando a cláusula raise com uma mensagem
#indicando que o triângulo informado é inválido.

import math

def menu(value):
    for i in range(0, 2, 1):
        sides = float(input("Digite os valores dos lados do triângulo:"))
        value.append(sides)
        
    base = float(input("Digite o valor da base do triângulo:"))   
    value.append(base)
    print(value)
    return value

def introduce(value):
    if value[0] == value[1] == value[2]:
        print("O triângulo é equilátero!")
    elif value[0] == value[1] != value[2] or value[0] != value[1] == value[2] or value[0] == value[2] != value[1]:
        print("O triângulo é isosceles!")
    elif value[0] != value[1] != value[2]:
        print("O triângulo é escaleno!")
    

def perimeter(value):
    p = sum(value)
    s = p / 2
    print("O perímetro do triângulo é: ", p)
    print("O semipeímetro do triângulo é: ", s)
    return s
    
    
def area(semi_perimetro, value):
    termos = [(semi_perimetro - lado) for lado in value]
    area = math.sqrt(semi_perimetro * termos[0] * termos[1] * termos[2])
    print("A área do triângulo é: ", area)
    return area

def height(area_do_triangulo, value):
    h = (area_do_triangulo * 2) / value[2]
    print("A altura do triângulo é: ", h)

def main():
    value = []
    menu(value)
    introduce(value)
    semi_perimetro = perimeter(value)
    area_do_triangulo = area(semi_perimetro, value)
    height(area_do_triangulo, value)    

main()
