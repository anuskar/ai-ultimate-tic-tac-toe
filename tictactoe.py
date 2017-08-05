"""
Ultimate Tic Tac Toe game tree solver.
"""

from engine.GameTree import GameTree
from UTTTState import UTTTState

"""
Entry point for Ultimate Tic Tac Toe game tree demo.
"""
def main():
    # Instantiate a game tree.
    game = GameTree(UTTTState())
    game.attach_turn_handler(None)

    i_won = game.play()
    if i_won:
        print("I won. Opponent lost.")
    else:
        print("I lost. Opponent won.")


if __name__ == "__main__":
    main()
