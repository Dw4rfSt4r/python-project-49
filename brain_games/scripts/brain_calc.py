#!/usr/bin/env python3
from brain_games.game_engine import cycle_game
from brain_games.games.brain_calc import start_calc, rules


def main():
    cycle_game(return_foo=start_calc, rules=rules)


if __name__ == '__main__':
    main()
