#функции
def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    result = one + delimiter + two
    print(result)
    # print(type(result))
get_summ(3, "мир")

def add(x, y):
    return (x + y)
r = add("learn ", "python")
print(r.upper())
