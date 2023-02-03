# Задаем длину списка наполненного рандомными числами от 1 до 100. 
# Вводим искомое число X.
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению.
import numpy as np
import random
import math

length_list = int(input(">> Enter length of list -> "))
li = np.random.randint(1, 101, length_list)
print(li)
x = int(input(">> Enter a number -> "))
counter = 0
for i in li:
    if i == x:
        counter += 1
if counter == 0:
    min_difference = abs(li[0] - x)
    index = 0
    for i in range(1, len(li)):
        if abs(li[i] - x) < min_difference:
            min_difference = abs(li[i] - x)
            index = i
    print(f'>> This number is not found. The nearest number to this number is {li[i]}')
else:
    print(f'>> This number occurs {counter} times')


