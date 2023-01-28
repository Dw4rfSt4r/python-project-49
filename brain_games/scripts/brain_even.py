#!/usr/bin/env python3
from brain_games.game_engine import cycle_game
from brain_games.games.brain_even import start_even, rules


def main():
    cycle_game(return_foo=start_even, rules=rules)


if __name__ == '__main__':
    main()
