#!/usr/bin/env python3
from brain_games.game_engine import play_game
from brain_games.games.brain_gcd import start_gcd, rules


def main():
    play_game(game=start_gcd, rules=rules)


if __name__ == '__main__':
    main()
