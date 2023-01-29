#!/usr/bin/env python3
from brain_games.game_engine import play_game
from brain_games.games.brain_progression import start_progression, rules


def main():
    play_game(game=start_progression, rules=rules)


if __name__ == '__main__':
    main()
