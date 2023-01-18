#!/usr/bin/env python3
from random import randint


def start_progression():
    rand_progression_start = randint(1, 10)
    rand_progression_stop = rand_progression_start + 10
    step = randint(1, 10)
    rand_progression = []
    for element in range(rand_progression_start, rand_progression_stop):
        rand_progression.append(rand_progression_start)
        rand_progression_start = rand_progression_start + step
    correct_element = randint(0, 9)
    correct_answer = str(rand_progression[correct_element])
    rand_progression[correct_element] = '..'
    progression_string = ''
    for element in rand_progression:
        progression_string = progression_string + ' ' + str(element)
    print('What number is missing in the progression?')
    print('Question:' + progression_string)
    return correct_answer


def main():
    start_progression()


if __name__ == '__main__':
    main()
