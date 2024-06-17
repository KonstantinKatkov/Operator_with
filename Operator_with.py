file_name = 'text_7_2.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line, end='')
