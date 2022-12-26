#!/usr/bin/env python3

from brain_games_cat import cli

greeting = 'Welcome to the Brain Games! '

def greet():
    print(greeting)

def main():
    greet()
    cli.welcome_user()

if __name__ == '__main__':
    main()

