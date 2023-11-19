# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.

n = 16


def print_powers_of_two(n):
    power = 0
    result = 1

    while result <= n:
        print(result)
        power += 1
        result = 2 ** power


print_powers_of_two(n)
