# CSC384
## Ultimate Tic Tac Toe

Python 3.5.2

## How To Run

```
python tictactoe.py
```

## How To Test

TODO

## Engine

There are 3 key classes, GameTree, UTTTSpace, and UTTTState.

### engine/GameTree.py

An implementation of a depth limited game tree, able to use custom heuristics and alpha-beta pruning, as well as invoke handlers to interact with a user or other AI. All of the game tree traversal, search, and evaluation functions are invoked or reside in this class.

The Game Tree can be supplied with any starting State, as well as an indication of whether the game tree's AI should go first, or if the opponent should make the first move.

### UTTTSpace

This class provides an easy way to interact with a Ultimate Tic Tac Toe board. It also keeps track of win conditions. Capable of supporting any size "Ultimate Tic Tac Toe" board (as long as it's square in nature).

### UTTTState

Binds the board, the turn, and any restrictions (such as where a player can go next) together in the form of the a node in the game tree.

## Heuristics

A utility value of 100 indicates a win for the AI, while -100 is a lose. In order to remain an admissible heuristic, the heuristic function should return values in the range [-100, 100].

### Heuristic A

- Stratigy 1: Count the number of win of subgame. More win in subgame, a higher utility will be assigned.
- Stratigy 2: Assign an utility value to each position on the game board. For example, take the middle block of the main gameboard and sub gameboard will have higher utility
- Stratigy 3: Consider the case of two out of three blocks are occupied by the same player. Then we will have higher utility to occupied that third sopt.
- Stratigy 4: In out turn a positive utility will be assigned; In opponent's turn a negetive utility will be assigned. It's because of the stratigy of alpha-beta pruning

### Heuristic B
Heuristic fuction B is a simplified version of Heuristic function A. It removes the Stratigy 3 from function A, but seems have better perfornmence.

## Comments

TODO
