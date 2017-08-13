# CSC384
## Ultimate Tic Tac Toe

__Developed By__

- Noah Negin-Ulster
- Zidong Xie

## System Requirements

Python 3.5.2

No external or third party libraries are used. To run the engine in an interactive mode (e.g. human vs AI), a terminal is required.

## How To Test

To run the heuristic comparison code, execute:

```
python compare_heuristics.py [--trace] [--dictate]
```

Passing in `--trace` will print the current execution. Passing in `--dictate` will print the current move.

To play against the engine yourself (human vs. AI), execute:

```
python tictactoe.py [--no-trace] [--computer-first] [--heuristic=A] [--depth=2] [--non-interactive=random]
```

Passing in `--computer-first` will cause the AI to make the first move. Note that this is the most computationally intensive part of the game due to the initial branching factor of `(n x N)^2` where `n` is the dimension of the inner subboard and `N` is the dimension of the outer board in terms of the number of subboards.

You may force a specific heuristic using the `--heuristic=#` flag. Refer to the heuristics list below for the heuristic IDs (all uppercase).

You may also specify a `non-interactive` function to use if you don't want to manually play the game. Options are:

- _random_: Picks a random move each turn.
- _first_: Always picks the first move in the successors list.
- _last_: Always picks the last move in the successors list.

## Engine

There are 3 key classes, GameTree, UTTTSpace, and UTTTState.

### engine/GameTree.py

An implementation of a depth limited game tree, able to use custom heuristics and alpha-beta pruning, as well as invoke handlers to interact with a user or other AI. All of the game tree traversal, search, and evaluation functions are invoked or reside in this class.

The Game Tree can be supplied with any starting State, as well as an indication of whether the game tree's AI should go first, or if the opponent should make the first move.

### UTTTSpace

This class provides an easy way to interact with an Ultimate Tic Tac Toe board. It also keeps track of win conditions. Capable of supporting any size "Ultimate Tic Tac Toe" board (as long as it's square in nature).

### UTTTState

Binds the board, the turn, and any restrictions (such as where a player can go next) together in the form of a node in the game tree.

## Heuristics

We have developed several heuristics which can be compared against each other by running `python compare_heuristics.py`.

Utility values are in the range [-100, 100] where 100 indicates a win for the AI, while -100 indicates a lose. All heuristic functions are restricted to this range to remain admissible.

### Heuristic A

__Only valid for a `N=3,n=3` game.__

This heuristic employs 4 overall _strategies_:

"Favouring" one factor over another implies that the favoured factor yields a higher utility value.

- __(S1)__: Favour a higher total count of the number of wins across all subgames.
- __(S2)__: Favour specific positions within both the outer game board and inner boards. Specifically favour the middle position in any board over sides or corners. A distribution of "weighted marks" is assigned to each position to indicates favoured cells.
- __(S3)__: Aim to _complete_ a row, column, or diagonal.
- __(S4)__: Ensure a zero-sum game by multiplying the utility value by a factor of -1 when computing the opponent's utility. This also enables proper use of alpha-benta pruning.

### Heuristic B

__Only valid for a `N=3,n=3` game.__

Identitical to Heuristic A, with the exception that __(S3)__ is removed in favour of higher performance (and thus greater depth limit can be used).

## Comments

TODO
