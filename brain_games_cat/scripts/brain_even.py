#!/usr/bin/env python3

from brain_games import greet, greeting
from basic_phrases import user_name, welcome, correct_answer, wrong_answer, good_game
from random import randint


def is_even(num):
    if num % 2:
        return 'no'
    else:
        return 'yes'

welcome()

print('Answer "yes" if the number is even, otherwise answer "no".')
i = 0
while i < 3:
    quiz_number = randint(1,100)
    print('Question:', quiz_number)
    quiz_answer = input('Your answer:')
    if quiz_answer == is_even(quiz_number):
        correct_answer()
        i = i + 1
    else:
        wrong_answer(quiz_answer, is_even(quiz_number))
        i = 5
if i == 3:
    good_game()