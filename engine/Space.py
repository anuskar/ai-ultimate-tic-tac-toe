"""
Represents part of the state space, e.g. the placement of game pieces.
For compact space complexity, each space object represents the delta
between its current "state" and its parent.
"""

from . import UnimplementedError

class Space:
    """
    Represents the abstract Space.
    """
    def __init__(self, parent=None):
        self.parent = parent


    def permutations(self):
        """
        Returns a list of all possible (loosely valid) permutations,
        using the current space configuration.
        """

        raise UnimplementedError()
