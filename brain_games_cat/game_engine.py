#!/usr/bin/env python3
from brain_games_cat.games.brain_even_logic import start_even
from brain_games_cat.games.brain_calc_logic import start_calc
from brain_games_cat.games.brain_gcd_logic import start_gcd
from brain_games_cat.games.brain_prime_logic import start_prime
from brain_games_cat.games.brain_progression_logic import start_progression

user_name = input('Welcome to the Brain Games!\nMay I have your name?')


def welcome():
    print('Hello, ' + user_name + '!')


rules = ['What is the result of the expression?', '\
Answer "yes" if the number is even, otherwise answer "no".', '\
Find the greatest common divisor of given numbers.', '\
Answer "yes" if given number is prime. Otherwise answer "no".', '\
What number is missing in the progression?']


def print_rules(game):
    if game == 'brain_gcd':
        print(rules[2])
    elif game == 'brain_prime':
        print(rules[3])
    elif game == 'brain_calc':
        print(rules[0])
    elif game == 'brain_progression':
        print(rules[4])
    elif game == 'brain_even':
        print(rules[1])


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


def print_is_correct_iterate(user_answer, correct_answer):
    correct_answer = str(correct_answer)

    if user_answer == correct_answer:
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


def compliment():
    print('Congratulations, ' + user_name + '!')


def cycle_game(game):
    ROUND_NUMBER = 3
    i = 0
    print_rules(game)
    while i < ROUND_NUMBER:
        correct_answer = choose_correct_answer(game)
        user_answer = get_user_answer()
        counter_breaker = print_is_correct_iterate(user_answer, correct_answer)
        if counter_breaker is False:
            break
        i = i + counter_breaker
    if i == ROUND_NUMBER:
        compliment()


def main():
    game = 'brain_even'
    user_name
    welcome
    cycle_game(game)


if __name__ == '__main__':
    main()
