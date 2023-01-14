#!/usr/bin/env python3
from random import randint
import brain_games_cat.scripts.game_engine


def main():
    brain_games_cat.scripts.game_engine.user_name
    brain_games_cat.scripts.game_engine.welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    round_number = 3
    correct_answer = ''
    while i < round_number:
        num = randint(2, 3571)
        if num == 2 or num == 3 or num == 5 or num == 7 or num == 11 or num == 13:
            correct_answer = 'yes'
        elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0 or num % 13 == 0:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'
        print('Question:', num)
        user_answer = input('Your answer:')
        counter = brain_games_cat.scripts.game_engine.check_solution(user_answer, correct_answer)
        i = i + counter  # check_solution() returns counter (1 or 5)
    if i == round_number:
        brain_games_cat.scripts.game_engine.good_game()


if __name__ == '__main__':
    main()
