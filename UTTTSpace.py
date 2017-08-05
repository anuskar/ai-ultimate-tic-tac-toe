from engine.Space import Space

"""
Represents the NxN grid composing the game board.
Each NxN grid is divided into nxn subboards.
"""
class UTTTSpace(Space):
    def __init__(self, parent = None, N = 3, n = 3):
        super().__init__(parent)

        self.cells = None
        self.N = N # dim of main board
        self.n = n # dim of subboard

        if parent is None:
            # Board is root node. Creating empty board.
            # note: 0,0 is top-left corner.
            self.cells = [[None for x in range(N)] for y in range(N)]
        else:
            # We inherit N and n from the parent if defined.
            self.N = parent.N
            self.n = parent.n





