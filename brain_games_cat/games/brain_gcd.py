#!/usr/bin/env python3
from math import gcd
from random import randint
from brain_games_cat.scripts.game_engine import user_name, welcome
from brain_games_cat.scripts.game_engine import check_solution, good_game


def main():
    user_name
    welcome()
    i = 0
    round_number = 3
    while i < round_number:

        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        correct_answer = gcd(num_1, num_2)
        print('Find the greatest common divisor of given numbers.')
        print('Question:', num_1, num_2)
        user_answer = input('Your answer: ')
        counter_breaker = check_solution(user_answer, correct_answer)
        i = i + counter_breaker
        # check_solution() returns counter_breaker == 1 or counter_breaker == 42
    if i == round_number:
        good_game()


if __name__ == '__main__':
    main()
