#цикл while

def hello_user(user_say):
    while True:
        if user_say == 'Хорошо':
            print('Всего хорошего')
            break
        else:
            print('Неправильно')
            user_say = input('Как дела? ')


user = input('Как дела? ')
hello_user(user)

#2
question = {
            'Как дела?': 'Хорошо!',
            'Что делаешь?': 'Программирую'
}

def ask_user(user):
    while True:
        if user == 'Как дела?':
            print(question['Как дела?'])
            break
        if user == 'Что делаешь?':
            print(question['Что делаешь?'])
            break
        else:
            print('Неправильно')
            user = input('Задай вопрос: "Как дела?" или "Что делаешь?" ')

user = input(' Задай вопрос: "Как дела?" или "Что делаешь?" ')
ask_user(user)
