#!/usr/bin/env python3

from random import randint
import brain_games_cat.scripts.game_engine


def main():
    brain_games_cat.scripts.game_engine.user_name
    brain_games_cat.scripts.game_engine.welcome()

    i = 0
    round_number = 3
    while i < round_number:
        num_1 = randint(1, 100)
        num_2 = randint(1,100)
        print('What is the result of the expression?','\nQusestion: ', num_1, '+', num_2)

        user_answer = input()
        correct_answer = str(sum([num_1, num_2]))
        if user_answer == correct_answer:
            print('Correct!')
            i = i + 1
            if i == round_number:
                brain_games_cat.scripts.game_engine.good_game()
        else:
            print(user_answer, 'is wrong answer ;(. Correct answer was "', correct_answer, '". Let\'s try again,', brain_games_cat.scripts.game_engine.user_name
        , '!')
            i = i + round_number + 1
            
if __name__ == '__main__':
    main()
