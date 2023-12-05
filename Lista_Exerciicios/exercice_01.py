def verificar_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Triângulo inválido. A soma de dois lados deve ser maior que o terceiro.")
    
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
