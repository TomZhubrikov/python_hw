# Требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no
def sum_digit(num):
    hundreds = int(num / 100)
    dozens = int(num / 10 % 10)
    units = int(num % 10)
    return hundreds + dozens + units


# Проверка на правильность ввода
F = True
while F:
    number = int(input('Enter a six-digit number -> '))
    if 99999 < number < 1000000:
        F = False

left_side = int(number / 1000)
right_side = int(number % 1000)

if sum_digit(left_side) == sum_digit(right_side):
    print('yes')
else:
    print('no')
