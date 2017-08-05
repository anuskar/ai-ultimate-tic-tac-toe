"""
Ultimate Tic Tac Toe State implementation.
"""

from engine.State import State

class UTTTState(State):
    """
    A representation of game state.
    """
    def __init__(self, turn=0, iSubboard=None, board=None):
        """
        Args:
            turn: 0 or 1, indicating which player decides the successor state.
            iSubboard:  The index of the subboard (1 of 9) which the turn player
                        must play in. Assigned left to right.
            board: a NxN grid with each cell holding a value of 0, 1, or None.
        """
        super().__init__()


    def successors(self):
        """

        """
        # must implement caching
        return []

    def is_winner(self, player_id):
        """

        """
        return None
