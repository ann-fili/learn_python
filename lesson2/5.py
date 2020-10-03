#Исключения
задание 1
def hello_user(user_say):
    while True:
        try:
            if user_say == 'Хорошо':
                print('Всего хорошего')
                break
            else:
                print('Неправильно')
                user_say = input('Как дела? ')
        except KeyboardInterrupt:
            print('Пока')
            break


user = input('Как дела? ')
hello_user(user)

#задание 2
def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount > 99:
            print('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except ValueError:
        print('Укажите числа')


try:
    discounted('ghgh', 1)
except TypeError:
    print('Неверное количество аргументов')


