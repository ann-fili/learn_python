#Создать список из десяти целых чисел.Вывести на экран каждое число, увеличенное на 1.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number + 1)

#Ввести с клавиатуры строку.Вывести эту же строку вертикально: по одному символу на строку консоли.
string = 'Строка'
for letter in string:
    print(letter)

#Создать список из словарей с оценками учеников разных классов
scores_class = [
    {'school_class': '3a', 'scores':[2,4,4,5,3]},
    {'school_class': '4a', 'scores':[3,4,5,5,2]},
    {'school_class': '5a', 'scores':[3,3,5,5,4]}
]
#Посчитать и вывести средний балл по всей школе.
scores_sum = 0
for class_ in scores_class:
    students_scores = class_['scores']
    for score in students_scores:
        scores_sum += score
scores_avg = (scores_sum / len(scores_class)) / len(students_scores)
print(f'Средняя оценка по школе {scores_avg} баллов')

#Посчитать и вывести средний балл по каждому классу.
def average():
    global scores_sum, score_, scores_avg
    scores_sum = 0
    for score_ in students_scores:
        scores_sum += score_
    scores_avg = scores_sum / len(students_scores)

for class_ in scores_class:
    students_class = class_['school_class']
    students_scores = class_['scores']
    if students_class == '3a':
        average()
        print(f'Средняя оценка по 3a классу {scores_avg} баллов')
    if students_class == '4a':
        average()
        print(f'Средняя оценка по 4a классу {scores_avg} баллов')
    if students_class == '5a':
        average()
        print(f'Средняя оценка по 5a классу {scores_avg} баллов')






