
age = int(input("Укажите возраст "))
def age_user(age):
    if  0 < age <= 6:
        return "Детский сад"
    elif 6 <= age <= 18:
        return "Школа"
    elif 18 <= age <= 24:
        return "Вуз"
    else:
        return "Работа"

print(age_user(age))


