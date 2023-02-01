# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.

# Пример:
# 10 -> 1 2 4 8

number = int(input("Enter a number (n > 0) -> "))
degree = 0
while 2 ** degree <= number:
    print(f'{2 ** degree}')
    degree += 1
