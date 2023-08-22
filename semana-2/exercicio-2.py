def encontrar_duplicatas_e_unificar(lista):
    duplicados = []
    unificados = []
    elementos_vistos = []
    
    for elemento in lista:
        if elemento in elementos_vistos:
            duplicados.append(elemento)
        else:
            elementos_vistos.append(elemento)
            unificados.append(elemento)
    
    return duplicados, unificados

# Exemplo de uso
duplicatas = [1, 2, 2, 3, 4, 4, 5, 6, 6]
duplicados, unificados = encontrar_duplicatas_e_unificar(duplicatas)
print("Elementos duplicados:", duplicados)
print("Elementos unificados:", unificados)
