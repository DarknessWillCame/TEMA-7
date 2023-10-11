alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

with open('./Tema7_3_input.txt', 'r') as file:
    lines = file.readlines()
    count_letters = 0
    count_words = 0

    for line in lines:
        for word in line.strip():
            if word.lower() in alphabet:
                count_letters += 1
        count_words += len(line.split(' '))

    print('Input file contains:')
    print(f'{count_letters} letters')
    print(f'{count_words} letters')
    print(f'{len(lines)} lines')