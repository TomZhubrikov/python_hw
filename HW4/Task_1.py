# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# Пример:
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# (без ввода кол-ва элемантов множеств)
set_1 = input("Enter a size of first set -> ")
set_2 = input("Enter a size of second set -> ")

set_1 = set(set_1.split())
set_2 = set(set_2.split())
set_3 = set_1.intersection(set_2)
list_set = [int(num) for num in list(set_3)]
list_set.sort()
list_set = [str(num) for num in list_set]

res_str = f"Result -> {' '.join(list_set)}"
print(res_str)


