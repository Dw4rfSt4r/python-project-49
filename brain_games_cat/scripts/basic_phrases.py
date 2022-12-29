#!/usr/bin/env python3


user_name = input('Welcome to the Brain Games!\nMay I have your name?')


def welcome():
    print('Hello,', user_name, '!')


def correct_answer():
    print('Correct!')


def wrong_answer(a, b):
    print(a, 'is wrong answer ;(. Correct answer was "', b, '". Let\'s try again,', user_name, '!')


def good_game():
    print('Congratulations,', user_name)
