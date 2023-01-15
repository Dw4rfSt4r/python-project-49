#!/usr/bin/env python3
from random import randint
from brain_games_cat.scripts.game_engine import user_name, welcome
from brain_games_cat.scripts.game_engine import check_solution, good_game


def is_prime(num):
    correct_answer = 'yes'
    for element in range(2, int(num ** 1 / 2)):
        if num % element == 0:
            correct_answer = 'no'
    return correct_answer


def main():
    user_name
    welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    round_number = 3
    while i < round_number:
        correct_answer = ''
        num = randint(2, 3391)
        correct_answer = is_prime(num)
        print('Question:', num)
        user_answer = input('Your answer:')
        counter = check_solution(user_answer, correct_answer)
        i = i + counter  # check_solution() returns counter (1 or 5)
    if i == round_number:
        good_game()


if __name__ == '__main__':
    main()
