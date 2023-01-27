#!/usr/bin/env python3
from brain_games.game_engine import user_name, welcome, cycle_game,\
    ROUND_NUMBER, compliment
from brain_games.games.brain_even import rules, start_even


def main():
    user_name
    welcome(rules)
    ROUND_NUMBER
    i = 0
    result = True
    while i < ROUND_NUMBER and result is True:
        answers_and_questions = start_even()
        result = cycle_game(answers_and_questions, rules)
        i += 1
        if i == ROUND_NUMBER:
            compliment()


if __name__ == '__main__':
    main()
