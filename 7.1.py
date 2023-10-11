import re

def get_ofter_word(value):
    dictionary = {}
    for x in value:
        if x in dictionary: dictionary[x] = dictionary[x] + 1
        else: dictionary[x] = 1
    dictionary_to_list = list(dictionary.items())
    dictionary_to_list.sort(reverse=True, key=lambda x: x[1])

    return dictionary_to_list[0:1][0]

with open('./Tema7_1_text.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    content_without_spectial_chars = re.sub(r'[^a-zA-Zа-яА-я0-9]', ' ', content)
    content_without_double_spaces = re.sub(r' {2,}', ' ', content_without_spectial_chars)
    splitted_content = content_without_double_spaces.split(' ')
    often_word = get_ofter_word(splitted_content)
    print('Всего слов:', len(splitted_content))
    print(f'Чаще всего встречается слово "{often_word[0]}". Оно встречается {often_word[1]} раз(а)')
