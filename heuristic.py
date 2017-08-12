
from engine.GameTree import *
from UTTTState import *
from UTTTSpace import *

def heuristic_A(turn_id, node):
    """
        The node which have more child will get priority
        """

    grade = 0
    children = node.successors()
    if (node.turn == turn_id):
        grade += len(children)
    else:
        grade -= len(children)
    return grade


