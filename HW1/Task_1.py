# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# Проверка на правильность ввода
F = True
while F:
    number = int(input('Enter a three-digit number -> '))
    if 99 < number < 1000:
        F = False

# Решение без цикла
hundreds = int(number / 100)
dozens = int(number / 10 % 10)
units = int(number % 10)
result_sum = hundreds + dozens + units
print(result_sum)

