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
