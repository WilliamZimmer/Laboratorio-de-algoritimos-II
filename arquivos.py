import random

def generation_random_numbers(amount):
    my_file = open('aula-12-terca/random-numbers.txt', "w")

    for i in range(amount):
        random_number = random.randint(0, 100)
        my_file.write(str(random_number) + "\n")

    my_file.close()

def generation_random_numbers_writelines(amount):
    content_list = []

    for i in range(amount):
        random_number = random.randint(0, 100)
        content_list.append(str(random_number) + "\n")

    my_file = open("aula-12-terca/random-numbers.txt", "w")
    my_file.writelines(content_list)
    my_file.close()

def read_with_readline():
    my_file = open('aula-12-terca/random-numbers.txt', "r")
    print(my_file.readline())
    print(my_file.readline())
    print(my_file.readline())
    print(my_file.readline())
    my_file.close()

def avg_with_readline():
    my_file = open("aula-12-terca/random-numbers.txt", "r")
    sum_of_numbers = 0
    lines_count = 0
    # Get the next line
    line = my_file.readline()

    while line != "":
        lines_count += 1
        sum_of_numbers += int(line)
        # Get the next line
        line = my_file.readline()

    return sum_of_numbers / lines_count

def avg_with_for():
    my_file = open("aula-12-terca/random-numbers.txt", "r")
    sum_of_numbers = 0
    lines_count = 0

    for line in my_file:
        lines_count += 1
        sum_of_numbers += int(line)

    return sum_of_numbers / lines_count

def avg_with_readlines():
    my_file = open("aula-12-terca/random-numbers.txt", "r")
    lines_list = my_file.readlines()
    sum_of_numbers = 0

    for line in lines_list:
        sum_of_numbers += int(line)

    my_file.close()
    return sum_of_numbers / len(lines_list)

def main():
    generation_random_numbers(100)
    read_with_readline()
    average = avg_with_readline()
    print(f"A média dos números no arquivo é: {average}")

main()

