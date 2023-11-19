# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)


# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# Введите ваше решение ниже
def find_indices_in_range(lst, min_number, max_number):
    indices = [index for index, value in enumerate(lst) if min_number <= value <= max_number]
    return indices
result_indices = find_indices_in_range(list_1, min_number, max_number)
for index in result_indices:
    print(index)