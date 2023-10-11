with open('./Tema7_2_text.txt', 'a') as file:
    date = input('Введите дату: ')
    category = input('Введите категорию: ')
    sum = int(input('Введите сумму: '))

    file.write(f'{date}\t\t\t{category}\t\t\t{sum}\n')

with open('./Tema7_2_text.txt', 'r') as file:
    print('Учёт расходов:\n', file.read())
