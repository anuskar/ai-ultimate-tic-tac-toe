"""
Ultimate Tic Tac Toe State implementation.
"""

from engine.State import State

class UTTTState(State):
    """
    A representation of game state.
    """
    def __init__(self, turn=0, parent=None, board=None):
        """
        Args:
            turn: 0 or 1, indicating which player decides the successor state.
            iSubboard:  The index of the subboard (1 of 9) which the turn player
                        must play in. Assigned left to right.
            board: a NxN grid with each cell holding a value of 0, 1, or None.
        """
        super().__init__(turn, parent)

        self.cached_successors = None


    def create_child(self, turn, space):
        """
        Instantiates a new child linked to this instance,
        using the given space.

        Args:
            turn: 0 or 1, the turn of the new state.
            space: Space, the space to associate with the child state.
        """

        return UTTTState(turn, self, space)

    def is_winner(self, player_id):
        """
        Given a player_id, determines if this state
        is a terminal state in which that player wins.

        Args:
            player_id: 0 or 1

        Raises: Exception if not terminal state.

        Returns: boolean
        """

        if self.successors():
            raise NonTerminalError()

        # TODO: and is not draw...

        return self.turn == (1 - player_id)
