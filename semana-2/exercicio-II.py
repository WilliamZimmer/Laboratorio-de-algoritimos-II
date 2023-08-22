def encontrar_duplicatas_e_unificar(lista):
    duplicados = [] 
    unificados = [] 
    contagem = {} 
    
    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1
            if contagem[elemento] == 2:
                duplicados.append(elemento)
        else:
            contagem[elemento] = 1
            unificados.append(elemento)
    
    return duplicados, unificados

duplicatas = [1, 2, 2, 3, 4, 4, 5, 6, 6]
duplicados, unificados = encontrar_duplicatas_e_unificar(duplicatas)
print("Elementos duplicados:", duplicados)  
print("Elementos unificados:", unificados)  
