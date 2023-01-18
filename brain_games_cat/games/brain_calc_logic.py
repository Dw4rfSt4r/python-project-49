#!/usr/bin/env python3
import operator
from random import randint


def start_calc():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    addition = operator.add(num_1, num_2)
    multiplication = operator.mul(num_1, num_2)
    subtraction = operator.sub(num_1, num_2)
    question_var = [addition, multiplication, subtraction]
    correct_answer = question_var[randint(0, 2)]
    print('What is the result of the expression?')
    if correct_answer == question_var[0]:
        print('Question:', num_1, '+', num_2)
    elif correct_answer == question_var[1]:
        print('Question:', num_1, '*', num_2)
    elif correct_answer == question_var[2]:
        print('Question:', num_1, '-', num_2)
    return correct_answer


def main():
    start_calc()


if __name__ == '__main__':
    main()
