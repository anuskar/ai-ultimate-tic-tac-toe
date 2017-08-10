"""
Ultimate Tic Tac Toe implementation of the space.
"""

class UTTTSpace():
    """
    Represents the NxN grid composing the game board.
    Each NxN grid is divided into nxn subboards.
    """

    def __init__(self, parent=None, N=3, n=3):
        self.cells = None
        self.N = N # dim of main board
        self.n = n # dim of subboard
        self.winner = None

        if parent is None:
            # Board is root node. Creating empty board.
            # Keeping the cells in a single dimensional list allows for
            # valid "shallow" copying.
            self.cells = [None for c in range((n*N) ** 2)]
        else:
            # We inherit N and n from the parent if defined.
            self.N = parent.N
            self.n = parent.n
            self.cells = list(parent.cells)

    def get(self, coord):
        """
        Gets the value at (iX, iY) in subboard (sX, sY).
        """

        (sX, sY, iX, iY) = coord

        x = (sX * self.N) + iX
        y = (sY * self.N) + iY
        return self.cells[(self.N * self.n * y) + x]

    def set(self, coord, val):
        """
        Sets the value at (iX, iY) in subboard (sX, sY) to val.
        """

        (sX, sY, iX, iY) = coord

        x = (sX * self.N) + iX
        y = (sY * self.N) + iY
        self.cells[(self.N * self.n * y) + x] = val

        # Check if winning move.
        # TODO self.winner = ...

    def is_winner(self, player_id):
        """
        Given a player_id, determines if this state
        is a terminal state in which that player wins.

        Args:
            player_id: 0 or 1

        Returns: boolean
        """

        return self.winner == player_id


