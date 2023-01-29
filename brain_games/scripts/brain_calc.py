#!/usr/bin/env python3
from brain_games.game_engine import play
from brain_games.games.brain_calc import get_answer_and_question, RULES


def main():
    play(give_answer_and_question=get_answer_and_question, rules=RULES)


if __name__ == '__main__':
    main()
