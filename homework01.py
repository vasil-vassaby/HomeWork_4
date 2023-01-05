# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

while True:
    try:
        k = int(input('Введите натуральную степень k: '))
        if k > 0:
            break
    except:
        print('Введите натуральное число!')


def get_ratios(degree, min_val, max_val):
    koef = [randint(min_val, max_val) for i in range(degree+1)]
    return koef

def get_polynomial(list_ratios):
    poly = '+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(list_ratios) if j][::-1]). \
        replace('x^1', 'x').\
        replace('+-', '-').\
        replace('x^0', '').\
        replace('^2', '\u00B2')
    return poly

indexes = {'1': "\u00B9",
           '2': "\u00B2",
           '3': "\u00B3",
           '4': "\u2074",
           '5': "\u2075",
           '6': "\u2076",
           '7': "\u2077",
           '8': "\u2078",
           '9': "\u2079",
           }

ratios = get_ratios(k, -100, 100)
polynom1 = get_polynomial(ratios)
print(polynom1, '=0', sep='')

ratios1 = get_ratios(k, -100, 100)
polynom2 = get_polynomial(ratios1)
print(polynom2, '=0', sep='')


#with open('polynomial_1.txt', 'w') as data:
 #   data.write(polynom1)

#with open('polynomial_2.txt', 'w') as data:
 #   data.write(polynom2)