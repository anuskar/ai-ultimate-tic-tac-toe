"""
Ultimate Tic Tac Toe game tree solver.
"""

import random
import argparse

from engine.GameTree import GameTree
from UTTTState import UTTTState
from UTTTSpace import UTTTSpace
from heuristic import heuristic_A, heuristic_B

TRACE_CHILDREN = True

def user_turn_handler(node):
    """
    Turn handler which retrieves input from a human player.
    """

    sc = node.successors()
    if TRACE_CHILDREN:
        for i in range(len(sc)):
            print("#" + str(i), str(sc[i]))

    while True:
        try:
            index = int(input("Enter the move id ({} - {}): ".format(0, len(sc) - 1)))
            if index < 0 or index >= len(sc):
                print("Out of bounds.")
                continue
            return index
        except:
            print("Unable to read as integer.")
            pass

    return None

def always_choose_random_state(node):
    """
    Makes a random move.
    """
    return random.randint(0, len(node.successors()) - 1)

def always_choose_first_state(node):
    return 0

def always_choose_last_state(node):
    sc = node.successors()
    length = len(sc) - 1
    return length

"""
Entry point for Ultimate Tic Tac Toe game tree demo.
"""
def main():
    non_interactive = {
        'random': always_choose_random_state,
        'first': always_choose_first_state,
        'last': always_choose_last_state
    }
    heuristics = { 'A': heuristic_A, 'B': heuristic_B }

    parser = argparse.ArgumentParser(description='Runs the game engine.')
    parser.add_argument('--no-trace', dest='TRACE_CHILDREN', action='store_false', help='Disables full tracing of successor states.')
    parser.add_argument('--computer-first', dest='COMPUTER_FIRST', action='store_true', help='Makes the AI go first.')
    parser.add_argument('--heuristic', default='A', dest='heuristic', choices=heuristics.keys(), help='Selects a heuristic for the AI to move.')
    parser.add_argument('--depth', default=2, type=int, dest='depth', help='Depth limit for game tree.')
    parser.add_argument('--non-interactive', dest='noninteractive', choices=non_interactive.keys(), help='Use a non-interactive turn handler.')
    args = parser.parse_args()

    if args.depth <= 0:
        raise 'Depth must be positive.'

    TRACE_CHILDREN = args.TRACE_CHILDREN

    print("Using heuristic '{}' with depth '{}'.".format(args.heuristic, args.depth))

    # Force AI to be Player with id 0 always.
    initial_state = UTTTState(1 if args.COMPUTER_FIRST else 0, None, None, UTTTSpace(None, 3, 3))

    # Instantiates a game tree.
    game = GameTree(initial_state, args.COMPUTER_FIRST, args.depth)

    if args.noninteractive is not None:
        print("Using non-interactive turn handler: {}".format(args.noninteractive))
        game.attach_turn_handler(non_interactive[args.noninteractive])
    else:
        print("Using a human-input user turn handler.")
        game.attach_turn_handler(user_turn_handler)

    i_won = game.play(heuristics[args.heuristic])
    if i_won:
        print("Computer won. Human lost.")
    else:
        print("Computer lost. Human won.")


if __name__ == "__main__":
    main()
