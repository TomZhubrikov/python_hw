# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
#
# Пример:
# 4 -> 1 2 3 4
# 9

bushes = [int(num) for num in input("Введите массив чисел -> ").split()]

max_barry = -1
for i in range(len(bushes)):
    if i == len(bushes) - 1:
        if bushes[i - 1] + bushes[i] + bushes[0] > max_barry:
            max_barry = bushes[i - 1] + bushes[i] + bushes[0]
    elif bushes[i - 1] + bushes[i] + bushes[i + 1] > max_barry:
        max_barry = bushes[i - 1] + bushes[i] + bushes[i + 1]
print(max_barry)
