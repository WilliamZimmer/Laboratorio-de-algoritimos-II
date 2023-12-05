# Faça um programa contendo uma função que recebe como argumentos os nomes de dois arquivos. 
# O primeiro arquivo contém nomes de alunos e o segundo arquivo contém as notas dos alunos. 
# No primeiro arquivo, cada linha corresponde ao nome de um aluno.
# No segundo arquivo, cada linha corresponde às notas dos alunos (uma ou mais). 
# Assuma que as notas foram armazenadas como strings, e estão separadas umas das outras por espaços em branco. 
# Leia os dois arquivos e gere um terceiro arquivo que contém o nome do aluno seguido da média de suas notas.

def processar_notas(file1, file2, output_file):
    nomes = file1.readlines()
    notas_linhas = file2.readlines()

    resultados = []

    for i, linha in enumerate(notas_linhas):
        notas = list(map(int, linha.strip().split()))

        media = sum(notas) / len(notas)

        resultados.append(f"{nomes[i].strip()}: Notas: {notas}, Média: {media:.2f}")

    for resultado in resultados:
        print(resultado)

    with open(output_file, 'w') as output:
        for resultado in resultados:
            output.write(f"{resultado}\n")

file1_path = 'names.txt'
file2_path = 'notes.txt'
output_file_path = 'output.txt'

with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    processar_notas(file1, file2, output_file_path)

file1.close()
file2.close()
