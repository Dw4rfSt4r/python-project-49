#!/usr/bin/env python3
from brain_games.game_engine import play_game
from brain_games.games.brain_calc import start_calc, rules


def main():
    play_game(game=start_calc, rules=rules)


if __name__ == '__main__':
    main()
