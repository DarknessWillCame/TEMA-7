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
