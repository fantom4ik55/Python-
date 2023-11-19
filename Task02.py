# Задача 2: Найдите сумму цифр трехзначного числа.

# n = 123
# res = 0

 
# digit1 = n // 100
# digit2 = (n // 10) % 10
# digit3 = n % 10

 
# res = digit1 + digit2 + digit3

# # print("n =", n, "-> res =", res, "("+str(digit1), "+", str(digit2), "+", str(digit3)+")")
# print(res)




n = 123
res = n // 100 + (n // 10) % 10 + n % 10

print(res)
