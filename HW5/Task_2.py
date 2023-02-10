# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def rec_sum(a:int, b:int) -> int:
    if b == 1:
        return a + 1
    else:
        return rec_sum(a, b - 1) + 1

a = int(input("Enter two non-negative integers (a, b):\n>> a = "))
b = int(input(">> b = "))

print(rec_sum(a, b))