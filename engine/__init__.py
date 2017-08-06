"""
Game Engine
"""

class UnimplementedError(Exception):
    """Function must be implemented in the derived class."""

class NonTerminalError(Exception):
    """An unsupported action was attempted on a non-terminal state."""
