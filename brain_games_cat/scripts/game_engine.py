#!/usr/bin/env python3


user_name = input('Welcome to the Brain Games!\nMay I have your name?')
counter = 0

def welcome():
    print('Hello,', user_name, '!')

def check_solution(user_answer, correct_answer):
    
    if user_answer == correct_answer:
        print('Correct!')
        counter = 1
        return counter
    else:
        print(user_answer, 'is wrong answer ;(. Correct answer was "', correct_answer, '". Let\'s try again,', user_name, '!')
        counter = 5
        return counter

def good_game():
     print('Congratulations,', user_name)


def main():
    welcome()
    check_solution()


if __name__ == '__main__':
    main()

