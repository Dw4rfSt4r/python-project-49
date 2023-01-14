#!/usr/bin/env python3
import operator
from random import randint
import brain_games_cat.scripts.game_engine


def main():
    brain_games_cat.scripts.game_engine.user_name
    brain_games_cat.scripts.game_engine.welcome()

    i = 0
    round_number = 3
    while i < round_number:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        addition = operator.add(num_1, num_2)
        multiplication = operator.mul(num_1, num_2)
        subtraction = operator.sub(num_1, num_2)
        question_var = [addition, multiplication, subtraction]
        correct_answer = question_var[randint(0, 2)]
        print('What is the result of the expression?')
        if correct_answer == question_var[0]:
            print('Qusestion: ', num_1, '\+', num_2)
        elif correct_answer == question_var[1]:
            print('Qusestion:', num_1, '*', num_2)
        elif correct_answer == question_var[2]:
            print('Qusestion: ', num_1, '-', num_2)
        user_answer = input()
        counter = brain_games_cat.scripts.game_engine.check_solution(user_answer, correct_answer)
        # check_solution() returns counter == 1 or counter == 5
        i = i + counter
    if i == round_number:
        brain_games_cat.scripts.game_engine.good_game()


if __name__ == '__main__':
    main()
