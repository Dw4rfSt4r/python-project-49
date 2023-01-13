#!/usr/bin/env python3
from math import gcd
from random import randint
import brain_games_cat.scripts.game_engine

def main():
    
    brain_games_cat.scripts.game_engine.user_name
    brain_games_cat.scripts.game_engine.welcome()
    i = 0
    round_number = 3
    while i < round_number:
 
        num_1 = randint(1,100)
        num_2 = randint(1, 100)
        correct_answer = gcd(num_1, num_2)
        print('Find the greatest common divisor of given numbers.\nQuestion:', num_1, num_2)
        user_answer = input('Your answer: ')
        counter = brain_games_cat.scripts.game_engine.check_solution(user_answer, correct_answer)
        i = i + counter #check_solution() returns counter == 1 or counter == 5
    if i == round_number:    
        brain_games_cat.scripts.game_engine.good_game()

if __name__ == '__main__':
    main()
