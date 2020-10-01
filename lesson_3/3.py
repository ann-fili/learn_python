#работа с файлами

with open('referat.txt', 'r', encoding='utf-8') as f:
    file = f.read()
    print(file)

with open('referat.txt', 'r', encoding='utf-8') as f:
    string = 0 #строки
    words = 0 #слова
    for line in f:
        wordslist = line.split() #разбить строку на части
        string = string + 1 #количество строк
        words = words + len(wordslist) #количество слов
    print(f'в файле {string} строк')
    print(f'в файле {words} слов')

with open('referat.txt', 'r', encoding='utf-8') as old_file, open('referat2.txt', 'w') as new_file:
    replace_characters = old_file.read().replace('.', '!')
    new_file.write(replace_characters)


