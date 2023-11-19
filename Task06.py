# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.


n = 123456
def is_lucky_ticket(n):
    ticket_str = str(n)  
    if len(ticket_str) != 6:
        return False  

    first_half = sum(int(digit) for digit in ticket_str[:3])
    second_half = sum(int(digit) for digit in ticket_str[3:])

    return first_half == second_half

if is_lucky_ticket(n):
    print("yes")
else:
    print("no")
