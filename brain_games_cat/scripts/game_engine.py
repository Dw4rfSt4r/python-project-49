#!/usr/bin/env python3


user_name = input('Welcome to the Brain Games!\nMay I have your name?')


def welcome():
    print('Hello,', user_name, '!')

def check_solution(user_answer, correct_answer):
    if user_answer == correct_answer:
        print('Correct!')
        
        return 1
    else:
        print(user_answer, 'is wrong answer ;(. Correct answer was "', correct_answer, '". Let\'s try again,', user_name, '!')
        
        return 5

def good_game():
     print('Congratulations,', user_name)


def main():
    welcome()
    check_solution()


if __name__ == '__main__':
    main()

