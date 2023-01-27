#!/usr/bin/env python3
from brain_games.game_engine import user_name, welcome, cycle_game, ROUND_NUMBER, compliment
from brain_games.games.brain_gcd import RULES, start_gcd


def main():
    user_name
    welcome(RULES)
    ROUND_NUMBER
    RULES
    i = 0
    result = True
    while i < ROUND_NUMBER and result is True:
        answers_and_questions = start_gcd()
        result = cycle_game(answers_and_questions, RULES)
        i += 1
        if i == ROUND_NUMBER:
            compliment()


if __name__ == '__main__':
    main()
