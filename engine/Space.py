"""
Represents part of the state space, e.g. the placement of game pieces.
For compact space complexity, each space object represents the delta
between its current "state" and its parent.
"""
class Space:
    def __init__(self, parent=None):
        self.parent = parent

        if parent is None:
            # This Space is the empty game, or game at the starting
            # position.
