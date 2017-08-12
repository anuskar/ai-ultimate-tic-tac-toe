
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


def heuristic_B(turn_id, node):

    grade = 0

    children = node.successors()
    if (node.turn == turn_id):
        grade += len(children)
    else:
        grade -= len(children)

    # if this is my turn
    if (node.turn == turn_id):
        for k in node.space.subgames:
            if (node.space.subgames[k] != None):
                if (node.space.subgames[k] == turn_id):
                    grade += grade

    else:
        for k in node.space.subgames:
            if (node.space.subgames[k] != None):
                if (node.space.subgames[k] == 1 - turn_id):
                    grade -= grade

    coord = []
    parent = node.parent

    for move in parent.possible_moves():
        (_, _, iX, iY) = move
        # Warning, a full copy of the space occurs here.
        child = UTTTState(1 - parent.turn, parent, (iX, iY))
        if(child.restriction == node.restriction ):
            coord = [iX, iY]

    if (node.restriction != None and node.turn == turn_id):
        #check colum
        for cx in range(node.space.n):
            opponent = 0
            mine = 0
            for cy in range(node.space.n):
               if node.space.get((coord[0], coord[1], cx, cy)) == 1 - turn_id:
                   opponent += 1
               elif node.space.get((coord[0], coord[1], cx, cy)) == turn_id:
                   mine += 1
            if opponent == 2 and mine == 0:
                grade -= 5

        #check row
        for cy in range(node.space.n):
            opponent = 0
            mine = 0
            for cx in range(node.space.n):
               if node.space.get((coord[0], coord[1], cx, cy)) == 1 - turn_id:
                   opponent += 1
               elif node.space.get((coord[0], coord[1], cx, cy)) == turn_id:
                   mine += 1
            if opponent == 2 and mine == 0:
                grade -= 5

        # check diagonals
        cx = 0
        cy = 0
        opponent = 0
        mine = 0
        while (cx < 3 and cy < 3):
            if node.space.get((coord[0], coord[1], cx, cy)) == 1 - turn_id:
                opponent += 1
            elif node.space.get((coord[0], coord[1], cx, cy)) == turn_id:
                mine += 1
            cx += 1
            cy += 1
        if opponent == 2 and mine == 0:
            grade -= 5

        cx = 2
        cy = 2
        opponent = 0
        mine = 0
        while (cx >= 0 and cy >= 0):
            if node.space.get((coord[0], coord[1], cx, cy)) == 1 - turn_id:
                opponent += 1
            elif node.space.get((coord[0], coord[1], cx, cy)) == turn_id:
                mine += 1
            cx -= 1
            cy -= 1
        if opponent == 2 and mine == 0:
            grade -= 5


    return grade
