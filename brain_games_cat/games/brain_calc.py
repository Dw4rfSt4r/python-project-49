#!/usr/bin/env python3
import operator
from random import randint
from brain_games_cat.scripts.game_engine import user_name, welcome, check_solution, good_game


def main():
    user_name
    welcome()

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
            print('Question:', num_1, '+', num_2)
        elif correct_answer == question_var[1]:
            print('Question:', num_1, '*', num_2)
        elif correct_answer == question_var[2]:
            print('Question:', num_1, '-', num_2)
        user_answer = input()
        counter = check_solution(user_answer, correct_answer)
        # check_solution() returns counter == 1 or counter == 5
        i = i + counter
    if i == round_number:
        good_game()


if __name__ == '__main__':
    main()
