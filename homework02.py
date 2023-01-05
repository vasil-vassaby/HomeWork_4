# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('polynomial_1.txt', 'r') as data:
    poly_1 = data.readline()
    list_of_poly_1 = poly_1.replace('=0', '').replace('-', '+-').replace('x^2', '').replace('x', '').split('+')
    list_of_poly_1 = [s for s in list_of_poly_1 if s]
    list_of_poly_1 = list(map(int, list_of_poly_1))

with open('polynomial_2.txt', 'r') as data:
    poly_2 = data.readline()
    list_of_poly_2 = poly_2.replace('=0', '').replace('-', '+-').replace('x^2', '').replace('x', '').split('+')
    list_of_poly_2 = [s for s in list_of_poly_2 if s]
    list_of_poly_2 = list(map(int, list_of_poly_2))

def sum_polynomial(poly_1, poly_2):
    sum_koeff = reversed(list(map(sum, zip(poly_1, poly_2))))
    sum_poly = '+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(sum_koeff) if j][::-1]).\
        replace('x^1', 'x').\
        replace('+-', '-').\
        replace('x^0', '')
    return sum_poly

result_poly = sum_polynomial(list_of_poly_1, list_of_poly_2)

with open('polynomial_3.txt', 'w', encoding='utf-8') as data:
    data.write(result_poly + '=0')