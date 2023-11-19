# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.




def min_flips(coins):
    heads = coins.count(0)  # количество монеток, лежащих гербом вверх
    tails = coins.count(1)  # количество монеток, лежащих решкой вверх
    
    return min(heads, tails)  # возвращаем минимальное значение между количеством гербовых и решковых монеток

# Пример использования:
coins = [0, 1, 0, 0, 1, 1, 0, 1]
min_flips_count = min_flips(coins)
print(min_flips_count)  # выводит: 3 (требуется перевернуть 3 монетки)


