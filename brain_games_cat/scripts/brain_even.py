#!/usr/bin/env python3

from random import randint
import brain_games_cat.scripts.game_engine


def is_even(num): #  even? yes or no - quiz_answer
    if num % 2:
        correct_answer = 'no'
        return correct_answer
    else:
        correct_answer = 'yes'
        return correct_answer

def main():
    brain_games_cat.scripts.game_engine.user_name
    brain_games_cat.scripts.game_engine.welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        quiz_number = randint(1, 100)
        print('Question:', quiz_number)
        user_answer = str(input('Your answer:'))
        correct_answer = is_even(quiz_number)
        i = i + brain_games_cat.scripts.game_engine.check_solution(user_answer, correct_answer) #check_solution() returns 1 or 5
    if i == 3:    
        brain_games_cat.scripts.game_engine.good_game()


if __name__ == '__main__':
    main()