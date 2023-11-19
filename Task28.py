# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.


def recursive_sum(a, b):
    if b == 0:
        return a
    else:
        return recursive_sum(a + 1, b - 1)
        
a = 20
b = 20
print(recursive_sum(a, b))
