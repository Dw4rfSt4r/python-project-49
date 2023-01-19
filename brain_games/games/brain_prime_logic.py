#!/usr/bin/env python3
from random import randint


def start_prime():
    num = randint(2, 3391)
    print('Question:', num)
    correct_answer = 'yes'
    for element in range(2, int(num ** 1 / 2)):
        if num % element == 0:
            correct_answer = 'no'
    return correct_answer


def main():
    start_prime()


if __name__ == '__main__':
    main()
