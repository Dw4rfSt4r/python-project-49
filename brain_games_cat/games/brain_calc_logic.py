#!/usr/bin/env python3
import operator
from random import randint


def start_calc():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    operators = ['+', '-', '*']
    for current_operator in operators:
        current_operator = operators[randint(0, 2)]
    if current_operator == '+':
        calculations = operator.add(num_1, num_2)
        print('Question:', num_1, '+', num_2)
    elif current_operator == '-':
        calculations = operator.mul(num_1, num_2)
    elif current_operator == '*':
        print('Question:', num_1, '*', num_2)
        calculations = operator.sub(num_1, num_2)
        print('Question:', num_1, '-', num_2)
    correct_answer = calculations
    return correct_answer


def main():
    start_calc()


if __name__ == '__main__':
    main()
