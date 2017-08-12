
from engine.GameTree import *
from UTTTState import *
from UTTTSpace import *


mark = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 1, 2, 1, 1, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 3, 3, 3, 1, 1, 1],
        [1, 2, 1, 3, 4, 3, 1, 2, 1],
        [1, 1, 1, 3, 3, 3, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 1, 2, 1, 1, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]]


def heuristic_A(turn_id, node):

    grade = 0

    # The state with more child will get priority
    children = node.successors()
    if (node.turn == turn_id):
        grade += len(children)
    else:
        grade -= len(children)

    # if child win more subgame will get higher grade
    middle = 0
    if (node.turn == turn_id):
        for k in node.space.subgames:
            if (node.space.subgames[k] != None):
                if (node.space.subgames[k] == turn_id):
                    grade += 1
                if k == (1,1):
                    middle = 1


    else:
        for k in node.space.subgames:
            if (node.space.subgames[k] != None):
                if (node.space.subgames[k] == 1 - turn_id):
                    grade -= 1
                if k == (1,1):
                    middle = 1

    if middle == 1:
        mark = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 2, 1, 1, 2, 1, 1, 2, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 2, 2, 2, 1, 1, 1],
                [1, 2, 1, 2, 4, 2, 1, 2, 1],
                [1, 1, 1, 2, 2, 2, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 2, 1, 1, 2, 1, 1, 2, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1]]
    else:
        mark = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 0, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 2, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 0, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1]]


    # if the opponent already ocupy two connected block in a subgame, then don not choose that subgame again
    coord = []
    parent = node.parent

    for move in parent.possible_moves():
        (_, _, iX, iY) = move
        # Warning, a full copy of the space occurs here.
        child = UTTTState(1 - parent.turn, parent, (iX, iY))
        if(child.restriction == node.restriction ):
            coord = [iX, iY]

    #More middle block in the subgame will earn more grade
    if (node.turn == turn_id):
        for y in range(node.space.N * node.space.n):
            for x in range(node.space.N * node.space.n):
                cell = node.space.cells[(node.space.N * node.space.n * y) + x]
                if cell == turn_id:
                    grade += mark[y][x]
    else:
        for y in range(node.space.N * node.space.n):
            for x in range(node.space.N * node.space.n):
                cell = node.space.cells[(node.space.N * node.space.n * y) + x]
                if cell == 1 - turn_id:
                    grade -= mark[y][x]

    # if in a sub game, two of mine nodes are connected, then it will have a higher gread
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
            if mine == 2 and opponent == 0:
                grade += 1

        #check row
        for cy in range(node.space.n):
            opponent = 0
            mine = 0
            for cx in range(node.space.n):
               if node.space.get((coord[0], coord[1], cx, cy)) == 1 - turn_id:
                   opponent += 1
               elif node.space.get((coord[0], coord[1], cx, cy)) == turn_id:
                   mine += 1
            if mine == 2 and opponent == 0:
                grade += 1

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
        if mine == 2 and opponent == 0:
            grade += 1

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
        if mine == 2 and opponent == 0:
            grade += 1


    #if two of opponent blockes are connected, then get lower gread
    if (node.restriction != None and node.turn == 1 - turn_id):
        #check colum
        for cx in range(node.space.n):
            opponent = 0
            mine = 0
            for cy in range(node.space.n):
               if node.space.get((coord[0], coord[1], cx, cy)) == turn_id:
                   opponent += 1
               elif node.space.get((coord[0], coord[1], cx, cy)) == 1 - turn_id:
                   mine += 1
            if opponent == 2 and mine == 0:
                grade -= 1

        #check row
        for cy in range(node.space.n):
            opponent = 0
            mine = 0
            for cx in range(node.space.n):
               if node.space.get((coord[0], coord[1], cx, cy)) == turn_id:
                   opponent += 1
               elif node.space.get((coord[0], coord[1], cx, cy)) == 1 - turn_id:
                   mine += 1
            if opponent == 2 and mine == 0:
                grade -= 1

        # check diagonals
        cx = 0
        cy = 0
        opponent = 0
        mine = 0
        while (cx < 3 and cy < 3):
            if node.space.get((coord[0], coord[1], cx, cy)) == turn_id:
                opponent += 1
            elif node.space.get((coord[0], coord[1], cx, cy)) == 1 - turn_id:
                mine += 1
            cx += 1
            cy += 1
        if opponent == 2 and mine == 0:
            grade -= 1

        cx = 2
        cy = 2
        opponent = 0
        mine = 0
        while (cx >= 0 and cy >= 0):
            if node.space.get((coord[0], coord[1], cx, cy)) == turn_id:
                opponent += 1
            elif node.space.get((coord[0], coord[1], cx, cy)) == 1 - turn_id:
                mine += 1
            cx -= 1
            cy -= 1
        if opponent == 2 and mine == 0:
            grade -= 1


    return grade


# selection of more useful heuristic from function heuristic_A
def heuristic_B(turn_id, node):
    grade = 0

    # The state with more child will get priority
    children = node.successors()
    if (node.turn == turn_id):
        grade += len(children)
    else:
        grade -= len(children)


    # check whether the middle subgame is won by anyone
    middle = 0
    for k in node.space.subgames:
        if (node.space.subgames[k] != None):
            if k == (1,1):
                middle = 1

    if middle == 1:
        mark = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 2, 1, 1, 2, 1, 1, 2, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 2, 2, 2, 1, 1, 1],
                [1, 2, 1, 2, 4, 2, 1, 2, 1],
                [1, 1, 1, 2, 2, 2, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 2, 1, 1, 2, 1, 1, 2, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1]]
    else:
        mark = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 0, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 2, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 0, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1]]

    #More middle block in the subgame will earn more grade
    if (node.turn == turn_id):
        for y in range(node.space.N * node.space.n):
            for x in range(node.space.N * node.space.n):
                cell = node.space.cells[(node.space.N * node.space.n * y) + x]
                if cell == turn_id:
                    grade += mark[y][x]

    else:
        for y in range(node.space.N * node.space.n):
            for x in range(node.space.N * node.space.n):
                cell = node.space.cells[(node.space.N * node.space.n * y) + x]
                if cell == 1 - turn_id:
                    grade -= mark[y][x]

    return grade
