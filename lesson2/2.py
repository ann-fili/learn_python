#Сравнение строк
def string(s1, s2):

    if type(s1) is not str or type(s2) is not str:
        return 0
    elif type(s1) or type(s2) is str:
        if len(s1) == len(s2):
            return 1
        elif len(s1) > len(s2):
            return 2
        elif len(s1) < len(s2):
            return 3
    else:
        raise ValueError('Какая то хня')

print(string(1, '1'))
print(string(1, True))
print(string(False, '1'))
print(string('True', '1'))
print(string(1, 1))
print(string('Hello', 'Hi'))
print(string('Hello', 'hello'))
print(string('Hi', 'Hello'))