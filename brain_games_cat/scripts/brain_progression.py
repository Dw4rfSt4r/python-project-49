#!/usr/bin/env python3
from random import randint
import brain_games_cat.scripts.game_engine


def main():
    brain_games_cat.scripts.game_engine.user_name
    brain_games_cat.scripts.game_engine.welcome()
    i = 0
    round_number = 3
    while i < round_number:
        rand_progression_start = randint(1, 50)
        rand_progression_stop = rand_progression_start + 10
        step = randint(0, 10)
        step_modificator = randint(0, 10)
        rand_progression = []
        for element in range(rand_progression_start, rand_progression_stop):
            rand_progression.append(element + step)
            step = step + step_modificator
        correct_element = randint(0, 9)
        correct_answer = str(rand_progression[correct_element])
        rand_progression[correct_element] = '..'
        progression_string = ''
        for element in rand_progression:
            progression_string = progression_string + ' ' + str(element)
        print('What number is missing in the progression?\nQuestion:' + progression_string)
        user_answer = input('Your answer: ')
        counter = brain_games_cat.scripts.game_engine.check_solution(user_answer, correct_answer)
        i = i + counter  # check_solution() returns counter == 1 or counter == 5
    if i == round_number:
        brain_games_cat.scripts.game_engine.good_game()


if __name__ == '__main__':
    main()
