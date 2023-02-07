# Сгенерировать 2 многочлена и сложить их.
# from typing import List
import numpy as np


def generator_of_input_polynomials(max_degree: int) -> str:
    polynomial = ""
    degree = max_degree
    while degree >= 0:
        coefficient = int(np.random.randint(-3, 4, 1))
        if coefficient == 0 and degree != 0:
            degree -= 1
            continue
        elif coefficient > 0:
            if degree > 1:
                if coefficient == 1:
                    term = f'x**{degree} + '
                else:
                    term = f'{coefficient}*x**{degree} + '
            elif degree == 1:
                if coefficient == 1:
                    term = 'x + '
                else:
                    term = f'{coefficient}*x + '
            else:
                term = f'{coefficient}'
        else:
            if degree > 1:
                if coefficient == -1:
                    term = f'(-x)**{degree} + '
                else:
                    term = f'({coefficient})*x**{degree} + '
            elif degree == 1:
                if coefficient == -1:
                    term = '(-x) + '
                else:
                    term = f'({coefficient})*x + '
            else:
                term = f'({coefficient})'
        polynomial += term
        degree -= 1
    polynomial += ' = 0'
    return polynomial


def get_key(term: str) -> str:
    key = ''
    flag = False
    for character in term:
        if character == 'x':
            flag = True
        elif flag:
            if character == ')':
                pass
            else:
                key += character
    if not flag:
        key = '**0'
    elif key == '':
        key = '**1'
    return '*x' + key


def get_value(term: str) -> str:
    value = ''
    for character in term:
        if character == '(':
            continue
        elif character == ')' or character == '*':
            break
        elif character == 'x':
            return '1'
        elif term[0:4] == '(-x)':
            return '-1'
        else:
            value += character
    return value


def creator_dict_of_coefficients(polynomial: str) -> dict:
    dict_of_coefficients: dict[str, str] = {}
    split_polynomial = polynomial.split()

    for term in range(0, len(split_polynomial) - 2, 2):
        dict_of_coefficients[get_key(split_polynomial[term])] = get_value(split_polynomial[term])
    return dict_of_coefficients


def get_summarise_of_polynomials() -> str:
    max_degree_1 = int(input(">> Enter a max degree of first polynomial -> "))
    polynom_1 = generator_of_input_polynomials(max_degree_1)
    print(polynom_1)
    dict_1 = creator_dict_of_coefficients(polynom_1)

    max_degree_2 = int(input(">> Enter a max degree of second polynomial -> "))
    polynom_2 = generator_of_input_polynomials(max_degree_2)
    print(polynom_2)
    dict_2 = creator_dict_of_coefficients(polynom_2)

    result_dict = {}
    if max_degree_1 > max_degree_2:
        i = max_degree_1
    else:
        i = max_degree_2

    while i >= 0:
        if f'*x**{i}' in dict_1 and f'*x**{i}' in dict_2:
            result_dict[f'*x**{i}'] = str(int(dict_1[f'*x**{i}']) + int(dict_2[f'*x**{i}']))
        elif f'*x**{i}' in dict_1:
            result_dict[f'*x**{i}'] = dict_1[f'*x**{i}']
        elif f'*x**{i}' in dict_2:
            result_dict[f'*x**{i}'] = dict_2[f'*x**{i}']
        else:
            i -= 1
            continue
        i -= 1

    # print(f'\n>> {result_dict}')

    result_polynomial = ''
    counter_interation = 0
    for key, value in result_dict.items():
        int_value = int(value)
        if int_value != 0:
            if counter_interation == 0:
                pass
            else:
                result_polynomial += ' + '
            if key == "*x**1":
                key = '*x'
            if key != "*x**0":
                if int_value > 0:
                    if int_value == 1:
                        result_polynomial += f'{key[1:]}'
                        counter_interation += 1
                    else:
                        result_polynomial += f'{value}{key}'
                        counter_interation += 1
                else:
                    if int_value == -1:
                        result_polynomial += f'(-x){key[2:]}'
                        counter_interation += 1
                    else:
                        result_polynomial += f'({value}){key}'
                        counter_interation += 1
            else:
                if int_value > 0:
                    result_polynomial += f'{value} = 0'
                else:
                    result_polynomial += f'({value}) = 0'
        else:
            if key == "*x**0":
                result_polynomial += ' = 0'
            else:
                pass
    return result_polynomial


print(f'Result >> {get_summarise_of_polynomials()}')
