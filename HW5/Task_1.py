# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии. >

def rec_degree (num: float, degree: int) -> float:
    if degree < 0:
        if degree == -1:
            return 1 / num
        else:
            return 1 / num * rec_degree(num, degree + 1)
    elif degree == 1:
        return num
    else:
        return num * rec_degree(num, degree - 1)

flag = True
while flag:
    try:
        number = float(input("Enter a number (for exit enter 'q') -> "))
        degree = int(input("Enter a degree -> "))
        print(rec_degree(number, degree))
    except ValueError:
        flag = False