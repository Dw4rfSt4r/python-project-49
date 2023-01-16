#!/usr/bin/env python3


user_name = input('Welcome to the Brain Games!\nMay I have your name?')
counter_breaker = 0


def welcome():
    print('Hello, ' + user_name + '!')


def check_solution(user_answer, correct_answer):
    correct_answer = str(correct_answer)

    if user_answer == (correct_answer):
        print('Correct!')
        counter_breaker = 1
        return counter_breaker
    else:
        print("'" + user_answer + "'", "is wrong answer ;(. Correct answer was \
'" + correct_answer + "'. Let\'s try again, " + user_name + '!')
        counter_breaker = 42
        return counter_breaker


def good_game():
    print('Congratulations, ' + user_name + '!')


def main():
    welcome()
    check_solution()


if __name__ == '__main__':
    main()
