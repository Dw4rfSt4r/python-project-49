#!/usr/bin/env python3
from brain_games.game_engine import user_name, welcome, cycle_game
from brain_games.games.brain_gcd import RULES, start_gcd


def main():
    RULES
    user_name
    welcome()
    answers_and_questions = start_gcd()
    cycle_game(answers_and_questions, RULES)


if __name__ == '__main__':
    main()
