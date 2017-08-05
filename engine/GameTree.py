"""
The 2-player game tree.
"""
class GameTree:
    def __init__(self, initial_state, opponent_first=False):
        self.current = initial_state
        self.turn_id = 1 if opponent_first else 0
        self.alpha = None
        self.beta = None

    def promptOpponent(self):
        pass

    def dictateMove(self, state):
        pass

    def play(self):
        while True:
            children = self.current.successors()
            if children is None:
                # If we reach a terminal node, then game is over.
                # Return True if we win.
                return self.current.turn == self.turn_id

            # Opponents turn.
            if self.current.turn != self.turn_id:
                # Keep asking for their move until a valid move is made.
                opponents_move = None
                while opponents_move not in children:
                    opponents_move = self.promptOpponent()

                self.current = opponents_move
                continue

            # Our turn.
            our_move = self.computeBestMove(children)

            # Tell opponent what we are doing.
            self.dictateMove(our_move)

            self.current = our_move

    def computeBestMove(self, options):
        pass
