import math


def print_playing_field(playing_field: list):
    string_view = f"{' '.join(playing_field)}"
    print(f"{string_view[:6]}\n{string_view[6:11]}\n{string_view[12:]}")


# def create_playing_field() -> list:
#     playing_field = []
#     for i in range(1, 19):
#         if i % 6 == 0 and i != 0:
#             playing_field.append('|')
#         elif i % 18 == 0 and i != 0:
#             playing_field.append(f'\n')
#         else:
#             playing_field.append(f' ')
#     return playing_field

def simple_create_playing_field() -> list:
    playing_field = ['-' for _ in range(9)]
    return playing_field


def bots_step(playing_field: list, bot_char: str):
    num_step = playing_field.count('x') + playing_field.count('0')
    if num_step == 0:
        print('>> Ход на 4 позицию!')
        playing_field[4] = f'{bot_char}'
    elif num_step == 2:
        index = playing_field.index('0')
        if index % 2 == 0:
            print(f'>> Ход на {abs(index - 8)} позицию!')
            playing_field[abs(index - 8)] = f'{bot_char}'
        elif index == 3 or index == 5:
            print(f'>> Ход на {index + 3} позицию!')
            playing_field[index + 3] = f'{bot_char}'
        elif index == 1 or index == 7:
            print(f'>> Ход на {index + 1} позицию!')
            playing_field[index + 1] = f'{bot_char}'
    elif num_step == 4:
        #
        if playing_field == ['-', '0', '0', '-', 'x', '-', 'x', '-', '-']:
            print(f'>> Ход на 0 позицию!')
            playing_field[0] = f'{bot_char}'
        elif playing_field == ['-', '-', '0', '-', 'x', '0', 'x', '-', '-']:
            print(f'>> Ход на 8 позицию!')
            playing_field[8] = f'{bot_char}'
        elif playing_field == ['0', '-', '0', '-', 'x', '-', 'x', '-', '-']:
            print(f'>> Ход на 1 позицию!')
            playing_field[1] = f'{bot_char}'
        elif playing_field == ['-', '-', '0', '-', 'x', '-', 'x', '-', '0']:
            print(f'>> Ход на 5 позицию!')
            playing_field[5] = f'{bot_char}'
        elif playing_field == ['-', '-', '0', '0', 'x', '-', 'x', '-', '-']:
            print(f'>> Ход на 7 позицию!')
            playing_field[7] = f'{bot_char}'
        elif playing_field == ['-', '-', '0', '-', 'x', '-', 'x', '0', '-']:
            print(f'>> Ход на 3 позицию!')
            playing_field[3] = f'{bot_char}'
        #
        elif playing_field == ['0', '0', '-', '-', 'x', '-', '-', '-', 'x']:
            print(f'>> Ход на 2 позицию!')
            playing_field[2] = f'{bot_char}'
        elif playing_field == ['0', '-', '-', '0', 'x', '-', '-', '-', 'x']:
            print(f'>> Ход на 6 позицию!')
            playing_field[6] = f'{bot_char}'
        elif playing_field == ['0', '-', '0', '-', 'x', '-', '-', '-', 'x']:
            print(f'>> Ход на 1 позицию!')
            playing_field[1] = f'{bot_char}'
        elif playing_field == ['0', '-', '-', '-', 'x', '-', '0', '-', 'x']:
            print(f'>> Ход на 3 позицию!')
            playing_field[3] = f'{bot_char}'
        elif playing_field == ['0', '-', '-', '-', 'x', '0', '-', '-', 'x']:
            print(f'>> Ход на 7 позицию!')
            playing_field[7] = f'{bot_char}'
        elif playing_field == ['0', '-', '-', '-', 'x', '-', '-', '0', 'x']:
            print(f'>> Ход на 5 позицию!')
            playing_field[5] = f'{bot_char}'
        #
        elif playing_field == ['-', '-', 'x', '0', 'x', '-', '0', '-', '-']:
            print(f'>> Ход на 0 позицию!')
            playing_field[0] = f'{bot_char}'
        elif playing_field == ['-', '-', 'x', '-', 'x', '-', '0', '0', '-']:
            print(f'>> Ход на 8 позицию!')
            playing_field[8] = f'{bot_char}'
        elif playing_field == ['0', '-', 'x', '-', 'x', '-', '0', '-', '-']:
            print(f'>> Ход на 3 позицию!')
            playing_field[3] = f'{bot_char}'
        elif playing_field == ['-', '-', 'x', '-', 'x', '-', '0', '-', '0']:
            print(f'>> Ход на 7 позицию!')
            playing_field[7] = f'{bot_char}'
        elif playing_field == ['-', '0', 'x', '-', 'x', '-', '0', '-', '-']:
            print(f'>> Ход на 5 позицию!')
            playing_field[5] = f'{bot_char}'
        elif playing_field == ['-', '-', 'x', '-', 'x', '0', '0', '-', '-']:
            print(f'>> Ход на 1 позицию!')
            playing_field[1] = f'{bot_char}'
        #
        elif playing_field == ['x', '-', '-', '-', 'x', '0', '-', '-', '0']:
            print(f'>> Ход на 2 позицию!')
            playing_field[2] = f'{bot_char}'
        elif playing_field == ['x', '-', '-', '-', 'x', '-', '-', '0', '0']:
            print(f'>> Ход на 6 позицию!')
            playing_field[6] = f'{bot_char}'
        elif playing_field == ['x', '-', '0', '-', 'x', '-', '-', '-', '0']:
            print(f'>> Ход на 5 позицию!')
            playing_field[5] = f'{bot_char}'
        elif playing_field == ['x', '-', '-', '-', 'x', '-', '0', '-', '0']:
            print(f'>> Ход на 7 позицию!')
            playing_field[7] = f'{bot_char}'
        elif playing_field == ['x', '0', '-', '-', 'x', '-', '-', '-', '0']:
            print(f'>> Ход на 3 позицию!')
            playing_field[3] = f'{bot_char}'
        elif playing_field == ['x', '-', '-', '0', 'x', '-', '-', '-', '0']:
            print(f'>> Ход на 1 позицию!')
            playing_field[1] = f'{bot_char}'
    elif num_step == 6:
        # Проверка на выигрышный ход
        if playing_field[2:7:2] == ['-', 'x', 'x']:
            print(f'>> Ход на 2 позицию! Ха-ха!')
            playing_field[2] = f'{bot_char}'
        elif playing_field[2:7:2] == ['x', 'x', '-']:
            print(f'>> Ход на 6 позицию! Ха-ха!')
            playing_field[6] = f'{bot_char}'
        elif playing_field[0:9:4] == ['-', 'x', 'x']:
            print(f'>> Ход на 0 позицию! Ха-ха!')
            playing_field[0] = f'{bot_char}'
        elif playing_field[0:9:4] == ['x', 'x', '-']:
            print(f'>> Ход на 8 позицию! Ха-ха!')
            playing_field[8] = f'{bot_char}'
        #
        elif playing_field[0:3] == ['x', 'x', '-']:
            print(f'>> Ход на 2 позицию! Ха-ха!')
            playing_field[2] = f'{bot_char}'
        elif playing_field[3:6] == ['x', 'x', '-']:
            print(f'>> Ход на 5 позицию! Ха-ха!')
            playing_field[5] = f'{bot_char}'
        elif playing_field[6:9] == ['x', 'x', '-']:
            print(f'>> Ход на 8 позицию! Ха-ха!')
            playing_field[8] = f'{bot_char}'
        elif playing_field[0:3] == ['-', 'x', 'x']:
            print(f'>> Ход на 0 позицию! Ха-ха!')
            playing_field[0] = f'{bot_char}'
        elif playing_field[3:6] == ['-', 'x', 'x']:
            print(f'>> Ход на 3 позицию! Ха-ха!')
            playing_field[3] = f'{bot_char}'
        elif playing_field[6:9] == ['-', 'x', 'x']:
            print(f'>> Ход на 6 позицию! Ха-ха!')
            playing_field[6] = f'{bot_char}'
        #
        elif playing_field[0:7:3] == ['x', 'x', '-']:
            print(f'>> Ход на 6 позицию! Ха-ха!')
            playing_field[6] = f'{bot_char}'
        elif playing_field[1:8:3] == ['x', 'x', '-']:
            print(f'>> Ход на 7 позицию! Ха-ха!')
            playing_field[7] = f'{bot_char}'
        elif playing_field[2:9:3] == ['x', 'x', '-']:
            print(f'>> Ход на 8 позицию! Ха-ха!')
            playing_field[8] = f'{bot_char}'
        elif playing_field[0:7:3] == ['-', 'x', 'x']:
            print(f'>> Ход на 0 позицию! Ха-ха!')
            playing_field[0] = f'{bot_char}'
        elif playing_field[1:8:3] == ['-', 'x', 'x']:
            print(f'>> Ход на 1 позицию! Ха-ха!')
            playing_field[1] = f'{bot_char}'
        elif playing_field[2:9:3] == ['-', 'x', 'x']:
            print(f'>> Ход на 2 позицию! Ха-ха!')
            playing_field[2] = f'{bot_char}'

        # Проверка на выиграшную позицию у соперника
        if playing_field[2:7:2] == ['-', '0', '0']:
            print(f'>> Ход на 2 позицию! Ха-ха!')
            playing_field[2] = f'{bot_char}'
        elif playing_field[2:7:2] == ['0', '0', '-']:
            print(f'>> Ход на 6 позицию! Ха-ха!')
            playing_field[6] = f'{bot_char}'
        elif playing_field[0:9:4] == ['-', '0', '0']:
            print(f'>> Ход на 0 позицию! Ха-ха!')
            playing_field[0] = f'{bot_char}'
        elif playing_field[0:9:4] == ['0', '0', '-']:
            print(f'>> Ход на 8 позицию! Ха-ха!')
            playing_field[8] = f'{bot_char}'
        #
        elif playing_field[0:3] == ['0', '0', '-']:
            print(f'>> Ход на 2 позицию! Ха-ха!')
            playing_field[2] = f'{bot_char}'
        elif playing_field[3:6] == ['0', '0', '-']:
            print(f'>> Ход на 5 позицию! Ха-ха!')
            playing_field[5] = f'{bot_char}'
        elif playing_field[6:9] == ['0', '0', '-']:
            print(f'>> Ход на 8 позицию! Ха-ха!')
            playing_field[8] = f'{bot_char}'
        elif playing_field[0:3] == ['-', '0', '0']:
            print(f'>> Ход на 0 позицию! Ха-ха!')
            playing_field[0] = f'{bot_char}'
        elif playing_field[3:6] == ['-', '0', '0']:
            print(f'>> Ход на 3 позицию! Ха-ха!')
            playing_field[3] = f'{bot_char}'
        elif playing_field[6:9] == ['-', '0', '0']:
            print(f'>> Ход на 6 позицию! Ха-ха!')
            playing_field[6] = f'{bot_char}'
        #
        elif playing_field[0:7:3] == ['0', '0', '-']:
            print(f'>> Ход на 6 позицию! Ха-ха!')
            playing_field[6] = f'{bot_char}'
        elif playing_field[1:8:3] == ['0', '0', '-']:
            print(f'>> Ход на 7 позицию! Ха-ха!')
            playing_field[7] = f'{bot_char}'
        elif playing_field[2:9:3] == ['0', '0', '-']:
            print(f'>> Ход на 8 позицию! Ха-ха!')
            playing_field[8] = f'{bot_char}'
        elif playing_field[0:7:3] == ['-', '0', '0']:
            print(f'>> Ход на 0 позицию! Ха-ха!')
            playing_field[0] = f'{bot_char}'
        elif playing_field[1:8:3] == ['-', '0', '0']:
            print(f'>> Ход на 1 позицию! Ха-ха!')
            playing_field[1] = f'{bot_char}'
        elif playing_field[2:9:3] == ['-', '0', '0']:
            print(f'>> Ход на 2 позицию! Ха-ха!')
            playing_field[2] = f'{bot_char}'

        # Ход в ничейной ситуации
        if playing_field[2:7:2] == ['-', 'x', '-']:
            print(f'>> Ход на 2 позицию!')
            playing_field[2] = f'{bot_char}'
        elif playing_field[0:9:4] == ['-', 'x', '-']:
            print(f'>> Ход на 0 позицию!')
            playing_field[0] = f'{bot_char}'
        #
        elif playing_field[0:3] == ['x', '-', '-']:
            print(f'>> Ход на 2 позицию!')
            playing_field[2] = f'{bot_char}'
        elif playing_field[3:6] == ['-', 'x', '-']:
            print(f'>> Ход на 3 позицию!')
            playing_field[3] = f'{bot_char}'
        elif playing_field[6:9] == ['x', '-', '-']:
            print(f'>> Ход на 8 позицию!')
            playing_field[8] = f'{bot_char}'
        elif playing_field[0:3] == ['-', '-', 'x']:
            print(f'>> Ход на 0 позицию!')
            playing_field[0] = f'{bot_char}'
        elif playing_field[6:9] == ['-', '-', 'x']:
            print(f'>> Ход на 6 позицию!')
            playing_field[6] = f'{bot_char}'
        #
        elif playing_field[0:7:3] == ['x', '-', '-']:
            print(f'>> Ход на 6 позицию!')
            playing_field[6] = f'{bot_char}'
        elif playing_field[1:8:3] == ['-', 'x', '-']:
            print(f'>> Ход на 7 позицию!')
            playing_field[7] = f'{bot_char}'
        elif playing_field[2:9:3] == ['x', '-', '-']:
            print(f'>> Ход на 8 позицию!')
            playing_field[8] = f'{bot_char}'
        elif playing_field[0:7:3] == ['-', '-', 'x']:
            print(f'>> Ход на 0 позицию!')
            playing_field[0] = f'{bot_char}'
        elif playing_field[2:9:3] == ['-', '-', 'x']:
            print(f'>> Ход на 2 позицию!')
            playing_field[2] = f'{bot_char}'
    elif num_step == 8:
        index = playing_field.index('-')
        print(f'>> Ход на {index} позицию!')
        playing_field[index] = f'{bot_char}'
    print_playing_field(playing_field)


def my_step(playing_field: list, my_char: str):
    flag = True
    while flag:
        pos = int(input("Ваш ход > "))
        if 0 <= pos <= 8:
            if playing_field[pos] != '-':
                print("!!! Эта позиции уже занята. Пожалуйста, выберете другую позицию.")
            else:
                flag = False
                playing_field[pos] = f'{my_char}'
        else:
            print("!!! Позиции с таким номером на поле нет. Выберете позицию с номером от 0 до 8.")
    print_playing_field(playing_field)


def test(playing_field: list):
    if playing_field[0:3] == ['x', 'x', 'x'] or playing_field[3:6] == ['x', 'x', 'x'] or playing_field[6:9] == ['x',
                                                                                                                'x',
                                                                                                                'x']:
        return 'x'
    elif playing_field[0:3] == ['0', '0', '0'] or playing_field[3:6] == ['0', '0', '0'] or playing_field[6:9] == ['0',
                                                                                                                  '0',
                                                                                                                  '0']:
        return '0'
    elif playing_field[0:7:3] == ['x', 'x', 'x'] or playing_field[1:8:3] == ['x', 'x', 'x'] or playing_field[2:9:3] == [
        'x', 'x', 'x']:
        return 'x'
    elif playing_field[0:7:3] == ['0', '0', '0'] or playing_field[1:8:3] == ['0', '0', '0'] or playing_field[2:9:3] == [
        '0', '0', '0']:
        return '0'
    elif playing_field[0:9:4] == ['x', 'x', 'x'] or playing_field[2:7:2] == ['x', 'x', 'x']:
        return 'x'
    elif playing_field[0:9:4] == ['0', '0', '0'] or playing_field[2:7:2] == ['0', '0', '0']:
        return '0'
    elif playing_field.count('-') == 0:
        return 'Ничья!'
    else:
        return '-'


def playing():
    first_step = input("Приветствуем, чемпиона!!!\nЧем будете играть? (-> 'x' если X, '0' если 0') -> ")
    if first_step == 'x':
        print(">> Хорошо! Удачи!\nИгра началась! Ваш ход первый.")
        bot_char = '0'
        my_char = 'x'
        step = 0
    else:
        print(">> Вы дали мне первый ход! У Вас нет шансов победить!\nИгра началась!")
        bot_char = 'x'
        my_char = '0'
        step = 1

    playing_field = simple_create_playing_field()
    print_playing_field(playing_field)

    count_step = 0
    while count_step < 9:
        if step == 0:
            my_step(playing_field, my_char)
            t = test(playing_field)
            if t == 'Ничья!':
                print(f"<< {t} >>!!!")
                break
            elif t == 'x' or t == '0':
                print(f"Победа << {t} >>!!!")
                break
            bots_step(playing_field, bot_char)
            t = test(playing_field)
            if t == 'Ничья!':
                print(f"<< {t} >>!!!")
                break
            elif t == 'x' or t == '0':
                print(f"Победа << {t} >>!!!")
                break
        else:
            bots_step(playing_field, bot_char)
            t = test(playing_field)
            if t == 'Ничья!':
                print(f"<< {t} >>!!!")
                break
            elif t == 'x' or t == '0':
                print(f"Победа << {t} >>!!!")
                break
            my_step(playing_field, my_char)
            t = test(playing_field)
            if t == 'Ничья!':
                print(f"<< {t} >>!!!")
                break
            elif t == 'x' or t == '0':
                print(f"Победа << {t} >>!!!")
                break
        count_step += 1


playing()
