#!/usr/bin/env python3
from random import randint


def start_even():
    num = randint(1, 100)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Question:', num)
    if num % 2 == 0:
        correct_answer = 'yes'
        return correct_answer
    else:
        correct_answer = 'no'
    return correct_answer


def main():
    start_even()


if __name__ == '__main__':
    main()
