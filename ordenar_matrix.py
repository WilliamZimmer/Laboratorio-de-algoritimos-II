my_list = [5, 9, 0]

for index in range(len(my_list)):
    for index_one in range(len(my_list)):
        if (index_one + 1) < len(my_list) and my_list[index_one] > my_list[index_one + 1]:
            tmp = my_list[index_one]
            my_list[index_one] = my_list[index_one + 1]
            my_list[index_one + 1] = tmp
        
        print(my_list)
    print('- - - - - - -- - - - - - - - - - - - - - - - - ')



##################################################################
lista = [5, 9, 0, 1, 2]
 for index_one in range(len(lista)):
    min_index = index_one

    for index_two in range(index_one, len(lista)):
        if lista[index_two] < lista[min_index]:
            min_index = index_two

    min_value = lista[min_index]
    lista[min_index] = lista[index_one]
    lista[index_one] = min_value

    print(lista)
    print("-------------------------------------")

##################################################################

matriz = [[5,9,0],
          [4,3,7],
          [1,2,6] ]


for line in range(len(matriz)):
    for column in range(len(matriz[line])):

        min_line = line
        min_column = column

        for line_aux in range(line, len(matriz)):

            start = column if line == line_aux else 0


            for column_aux in range(start, len(matriz[line_aux])):

                if matriz[line_aux][column_aux] < matriz[min_line][min_column]:

                    min_line = line_aux
                    min_column = column_aux

        #armazena o menor valor 
        min_value = matriz[min_line][min_column]
        #armazena na posiçao do menor valor o valor total
        matriz[min_line][min_column] = matriz[line][column]
        #armazena o valor atual o menor valor
        matriz[line][column] = min_value


        print(matriz)

for line in range(len(matriz)):
    for column in range(len(matriz[line])):
        print(matriz[line][column], end= ' ')
    print('')


