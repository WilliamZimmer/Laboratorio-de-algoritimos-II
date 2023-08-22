def encontrar_duplicatas_e_unificar(lista):
    duplicados = []
    unificados = []
    contagem = {}
    
    for elemento in lista:
        if elemento in ontagem:
            contagem[elemento] += 1
            if contagem[elemento] == 2:
                duplicados.append(elemento)
        else:
            contagem[elemento] = 1
            unificados.append(elemento)
    
    return duplicados, unificados

duplicatas = [1, 2, 2, 3, 4, 4, 5, 6, 6]
duplicatas, unificados = encontrar_duplicatas_e_unificar(lista_com_duplicatas)
print("Elementos duplicados:", duplicatas) 
print("Elementos unificados:", unificados)  
