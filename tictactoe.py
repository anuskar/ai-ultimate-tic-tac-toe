"""
Ultimate Tic Tac Toe game tree solver.
"""

from engine.GameTree import GameTree
from UTTTState import UTTTState
from UTTTSpace import UTTTSpace

def user_turn_handler(node):
    """
    Turn handler which retrieves input from a human player.
    """

    sc = node.successors()
    for i in range(len(sc)):
        print(i, str(sc[i]))

    while True:
        try:
            index = int(input("Enter the move id: "))
            if index < 0 or index >= len(sc):
                print("Out of bounds.")
                continue
            return index
        except TypeError:
            pass

    return None

"""
Entry point for Ultimate Tic Tac Toe game tree demo.
"""
def main():
    # Instantiate a game tree.
    opponent_first = False
    initial_state = UTTTState(1 if opponent_first else 0, None, UTTTSpace(None, 3, 3))
    game = GameTree(initial_state, 1 if opponent_first else 0)
    game.attach_turn_handler(user_turn_handler)

    i_won = game.play()
    if i_won:
        print("I won. Opponent lost.")
    else:
        print("I lost. Opponent won.")


if __name__ == "__main__":
    main()
