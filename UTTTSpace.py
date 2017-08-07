"""
Ultimate Tic Tac Toe implementation of the space.
"""

from engine.Space import Space

class UTTTSpace(Space):
    """
    Represents the NxN grid composing the game board.
    Each NxN grid is divided into nxn subboards.
    """

    def __init__(self, parent=None, N=3, n=3):
        super().__init__(parent)

        self.cells = None
        self.N = N # dim of main board
        self.n = n # dim of subboard

        if parent is None:
            # Board is root node. Creating empty board.
            # note: 0,0 is top-left subboard.
            # sX, sY are indices pointing to the subboard.
            # iX, iY are indices pointing to the cells within the subboard[sX, sY]
            self.cells = [[[[None for iX in range(n)] for iY in range(n)]
                           for sX in range(N)] for sY in range(N)]
        else:
            # We inherit N and n from the parent if defined.
            self.N = parent.N
            self.n = parent.n

    def permutations(self):
        """
        Returns a list of all possible (loosely valid) permutations,
        using the current space configuration.
        """

        pass


