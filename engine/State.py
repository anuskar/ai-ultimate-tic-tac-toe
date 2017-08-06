"""
Represents the game state, utilized as a tree node.
"""

from . import UnimplementedError, NonTerminalError

class State:
    """
    Abstract State class which represents the game space and turn. Also
    holds a reference to the parent state.
    """
    def __init__(self, turn, parent, space):
        self.turn = turn
        self.parent = parent
        self.space = space
        self.cached_successors = None

    def __str__(self):
        """
        Returns the string representation of this state.
        """

        return "Turn: {0}\n{1}".format(str(self.turn), str(self.space))

    def create_child(self, turn, space):
        """
        Instantiates a new child linked to this instance,
        using the given space.

        Args:
            turn: 0 or 1, the turn of the new state.
            space: Space, the space to associate with the child state.
        """
        raise UnimplementedError()

    def successors(self):
        """
        Returns a list of successor states.
        """

        if not self.cached_successors:
            children = []
            for p in self.space.permutations():
                child = None
                try:
                    child = self.create_child(1 - self.turn, p)
                except UnimplementedError:
                    # Assuming identical constructor signature. Dangerous.
                    child = self.__class__(1 - self.turn, self, p)

                if child:
                    children.append(child)

            self.cached_successors = children

        return self.cached_successors

    def is_winner(self, player_id):
        """
        Given a player_id, determines if this state
        is a terminal state in which that player wins.

        Args:
            player_id: 0 or 1

        Raises: Exception if not terminal state.

        Returns: boolean
        """

        raise UnimplementedError()
