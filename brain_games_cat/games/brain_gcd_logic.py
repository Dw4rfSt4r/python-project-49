#!/usr/bin/env python3
from math import gcd
from random import randint


def start_gcd():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    correct_answer = gcd(num_1, num_2)
    print('Question:', num_1, num_2)
    return correct_answer


def main():
    start_gcd()


if __name__ == '__main__':
    main()
