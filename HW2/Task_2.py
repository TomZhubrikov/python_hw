# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа 
# X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две 
# подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# Пример:
# 4 4 -> 2 2
# 5 6 -> 2

# Решение перебором
sum = int(input("Enter a sum of numbers -> "))
prod = int(input("Enter a product of numbers -> "))
first_number = 1
F = True
while first_number <= int(sum / 2) and F == True:
    if first_number * (sum - first_number) == prod:
        second_number = sum - first_number
        F = False
        print(f'Petya guessed the numbers {first_number} and {second_number}')
    first_number += 1
