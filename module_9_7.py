'''Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
Пример:
result = sum_three(2, 3, 6)
print(result)

Результат консоли:
Простое
11

Примечания:
Не забудьте написать внутреннюю функцию wrapper в is_prime
Функция is_prime должна возвращать wrapper
@is_prime - декоратор для функции sum_three

Файл module_9_7.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
'''

def is_prime(func):
    def wrapper(a,b,c):
        result=sum_three(a,b,c)
        k = 0
        for i in range(2, result // 2 + 1):
            if (result % i == 0):
                k = k + 1
        if (k <= 0):
            return "Число простое"
        else:
            return "Число не является простым"

    return wrapper



def sum_three(a,b,c):
    result=a+b+c
    print(result)
    return result

sum_three_1=is_prime(sum_three)
result = sum_three_1(2, 3, 6)
print(result)
