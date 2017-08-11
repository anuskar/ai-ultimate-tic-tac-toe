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

A utility value of 1 indicates a win for the AI, while -1 is a lose. In order to remain an admissible heuristic, the heuristic function should return values in the range [-1, 1].

### Heuristic A

- Based on the progress towards a win in the outer board, dictated by progress towards a win in each subboard.

## Comments

TODO
