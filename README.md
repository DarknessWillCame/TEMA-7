# Тема 7. Работа с файлами (Ввод\Вывод)
Отчет по Теме #7 выполнил(а):

- Черезов Роман Алексеевич
ЗПИЭ-20-1

| Задание   | Сам_раб |
|-----------|---------|
| Задание 1 | +       |
| Задание 2 | +       |
| Задание 3 | +       |
| Задание 4 | +       |
| Задание 5 | +       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.
```python
import re


def get_ofter_word(value):
    dictionary = {}
    for x in value:
        if x in dictionary:
            dictionary[x] = dictionary[x] + 1
        else:
            dictionary[x] = 1
    dictionary_to_list = list(dictionary.items())
    dictionary_to_list.sort(reverse=True, key=lambda x: x[1])

    return dictionary_to_list[0:1][0]


with open('Tema7_1_text.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    content_without_spectial_chars = re.sub(r'[^a-zA-Zа-яА-я0-9]', ' ', content)
    content_without_double_spaces = re.sub(r' {2,}', ' ', content_without_spectial_chars)
    splitted_content = content_without_double_spaces.split(' ')
    often_word = get_ofter_word(splitted_content)
    print('Всего слов:', len(splitted_content))
    print(f'Чаще всего встречается слово "{often_word[0]}". Оно встречается {often_word[1]} раз(а)')
```    
## Результат.
![Tema7_1](https://github.com/DarknessWillCame/TEMA-7/assets/46960566/2566f6c1-4622-472c-9573-6417770838ca)

Результат задания 1 

## Выводы
После чтения текста удалил знаки пунктуации
Затем удалил лишние пробелы
Разбил строку на отдельные слова при помощи функции split()
Дальше посчитал общее количество слов при помощи функции len() и самое частое слово при помощи словаря
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.
```python
with open('./Tema7_2_text.txt', 'a') as file:
    date = input('Введите дату: ')
    category = input('Введите категорию: ')
    sum = int(input('Введите сумму: '))

    file.write(f'{date}\t\t\t{category}\t\t\t{sum}\n')

with open('./Tema7_2_text.txt', 'r') as file:
    print('Учёт расходов:\n', file.read())
```    
## Результат.
![Tema7_2](https://github.com/DarknessWillCame/TEMA-7/assets/46960566/d8e17c43-5324-406f-952d-3f694d4381e1)

Результат задания 2 


## Выводы
С помощью режима добавления (a) вносится новая информация от пользователя
С помощью режима чтения (r) отображается ранее введёная информацию
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
```python
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
```
##Результат.
![Tema7_3](https://github.com/DarknessWillCame/TEMA-7/assets/46960566/265cb41c-a1f8-4bb6-8a8b-3396d321971e)

Результат задания 3

##Выводы
При помощи цикла можно посчитать все слова При помощи вложенного цикла можно посчитать все буквы При помощи функции len() можно посчитать количество строк

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
```python
example_1 = 'Hello, world! Python IS the programming language of thE future. My\nEMAIL is....\nPYTHON is awesome!!!!'

with open('./Tema7_4_input.txt', 'r') as file:
    words = file.read().split(' ')
    lower_text = example_1.lower()

    for word in words:
        lower_text = lower_text.replace(word, '*' * len(word))

    result = ''

    for index, word in enumerate(lower_text):
        if example_1[index].lower() == word:
            result += example_1[index]
        else:
            result += word

    print(result)
```
## Результат.
![Tema7_4](https://github.com/DarknessWillCame/TEMA-7/assets/46960566/659872ae-b8ab-46af-981a-f1d4848b3fac)

Результат задания 4

## Выводы
Сперва приводим строку к нижнему регистру и заменяем все необходимые слова на *
Затем востанавливаем регистр символов при помощи первоночальной строки
## Самостоятельная работа №5
### Имеется два файла с текстом. Необходимо поменять содержимое файла местами
```python
content_A = ''
content_B = ''

with open('./Tema7_5_A.txt', 'r') as file:
    content_A = file.read()

with open('./Tema7_5_B.txt', 'r') as file:
    content_B = file.read()

with open('./Tema7_5_A.txt', 'w') as file:
    file.write(content_B)

with open('./Tema7_5_B.txt', 'w') as file:
    file.write(content_A)
 ```   
## Результат.
![Tema7_5](https://github.com/DarknessWillCame/TEMA-7/assets/46960566/d5d7454e-33a5-4e02-bf97-fb56a9443e49)

Результат задания 5

## Выводы
Сначала нужно прочитать данные из файла и сохранить в переменную, а затем меняем их местами

## Общие выводы по теме
В ходе выполнения работы я выяснил, что Python имеет широкие возможности для работы с файлами. Можно создавать, читать, записывать. Чтение можно выполнять как целиком так и построчно
