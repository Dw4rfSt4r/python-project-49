#!/usr/bin/env python3
from random import randint
from brain_games_cat.scripts.game_engine import user_name, welcome, check_solution, good_game


def is_even(num):
    if num % 2:
        correct_answer = 'no'
        return correct_answer
    else:
        correct_answer = 'yes'
        return correct_answer


def main():
    user_name
    welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    round_number = 3
    while i < round_number:
        quiz_number = randint(1, 100)
        print('Question:', quiz_number)
        correct_answer = is_even(quiz_number)
        user_answer = input('Your answer:')
        counter = check_solution(user_answer, correct_answer)
        i = i + counter  # check_solution() returns counter (1 or 5)
    if i == round_number:
        good_game()


if __name__ == '__main__':
    main()
