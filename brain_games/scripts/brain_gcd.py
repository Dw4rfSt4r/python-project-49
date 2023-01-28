#!/usr/bin/env python3
from brain_games.game_engine import cycle_game
from brain_games.games.brain_gcd import start_gcd, rules


def main():
    cycle_game(return_foo=start_gcd, rules=rules)


if __name__ == '__main__':
    main()
