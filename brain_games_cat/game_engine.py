#!/usr/bin/env python3
from brain_games_cat.games.brain_even_logic import start_even
from brain_games_cat.games.brain_calc_logic import start_calc
from brain_games_cat.games.brain_gcd_logic import start_gcd
from brain_games_cat.games.brain_prime_logic import start_prime
from brain_games_cat.games.brain_progression_logic import start_progression

user_name = input('Welcome to the Brain Games!\nMay I have your name?')


def welcome():
    print('Hello, ' + user_name + '!')


def choose_correct_answer(game):
    if game == 'brain_gcd':
        correct_answer = start_gcd()
    elif game == 'brain_prime':
        correct_answer = start_prime()
    elif game == 'brain_calc':
        correct_answer = start_calc()
    elif game == 'brain_progression':
        correct_answer = start_progression()
    elif game == 'brain_even':
        correct_answer = start_even()
    return correct_answer


def check_solution(user_answer, correct_answer):
    correct_answer = str(correct_answer)

    if user_answer == (correct_answer):
        print('Correct!')
        counter_breaker = True
        return counter_breaker
    else:
        print("'" + user_answer + "'", "is wrong answer ;(. Correct answer was \
'" + correct_answer + "'. Let\'s try again, " + user_name + '!')
        counter_breaker = False
        return counter_breaker


def get_user_answer():
    user_answer = input('Your answer:')
    return user_answer


def play_game(game):
    ROUND_NUMBER = 3
    i = 0
    while i < ROUND_NUMBER:
        correct_answer = choose_correct_answer(game)
        user_answer = get_user_answer()
        counter_breaker = check_solution(user_answer, correct_answer)
        if counter_breaker is False:
            break
        i = i + counter_breaker
    if i == ROUND_NUMBER:
        print('Congratulations, ' + user_name + '!')


def main():
    game = 'brain_even'
    user_name
    welcome
    play_game(game)


if __name__ == '__main__':
    main()
