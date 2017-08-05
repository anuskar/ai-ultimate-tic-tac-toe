"""
Game Tree
"""

from . import State

class GameTree:
    """
    The 2-player game tree via a depth limited heuristic based MinMax.
    """
    def __init__(self, initial_state, opponent_first=False):
        """
        Args:
            initial_state: State.
            opponent_first: Boolean, indicates if the opponent makes the
                            first move.
        """

        self.current = initial_state
        self.custom_heuristic = None
        self.turn_handler = None

        self.turn_id = initial_state.turn
        if opponent_first:
            self.turn_id = 1 - initial_state.turn

        self.alpha = float("-inf")
        self.beta = float("inf")


    def attach_turn_handler(self, handler):
        """
        Attaches a turn handler which is invoked when it is the
        opponents turn. The handler should return the value of
        the next state, or optionally an integer representing
        the index into the current node's successor's list.

        Args:
            handler: A function invoked when it is the opponents
                    turn.
        """
        self.turn_handler = handler

    def prompt_opponent(self, node):
        """
        Prompts the opponent for their next move and returns that move.
        The move is "validated". If an invalid move is supplied, the opponent
        is prompted again.

        Args:
            node: The current State.

        Returns: a State instance.
        """

        if not self.turn_handler:
            raise "No turn handler defined."

        # Keep asking for their move until a valid move is made.
        valid_moves = node.successors()

        opponents_move = None
        while opponents_move not in valid_moves:
            opponents_move = self.turn_handler(node)
            if not isinstance(opponents_move, State):
                # Allow the handler to return an index into the successors list.
                opponents_move = valid_moves[opponents_move]

        return opponents_move

    def dictate_move(self, state):
        """
        Prints information about the current state.

        Args:
            state: The state to dictate.
        """

        print(state)

    def play(self, custom_heuristic=None):
        """
        Plays the game.

        Args:
            custom_heuristic: Function, an optional custom heuristic to
                              be applied for the depth limited MinMax.

        Returns: True if the opponent loses.
        """

        self.custom_heuristic = custom_heuristic

        while True:
            children = self.current.successors()
            if children is None:
                # If we reach a terminal node, then game is over.
                # Return True if we win.
                return self.current.turn == self.turn_id

            # Opponents turn.
            if self.current.turn != self.turn_id:
                opponents_move = self.prompt_opponent(self.current)

                self.current = opponents_move
                continue

            # Our turn.
            our_move = self.compute_best_move(self.current)

            # Tell opponent what we are doing.
            self.dictate_move(our_move)

            self.current = our_move


    def eval_heuristic(self, node):
        """
        Computes and returns the heuristic function applied to the node.

        Args:
            node: The node (State) to evaluate.

        Returns: h(node)
        """

        if self.custom_heuristic:
            return self.custom_heuristic(self.turn_id, node)

        # Otherwise use some default heuristic.
        return 0

    def utility(self, node):
        """
        Computes the utility value of the game tree node (State),
        by invoking the heuristic evaluation function.

        Args:
            node: The node to apply the utility function to.

        Returns the utility value of the node.
        """

        children = node.successors()
        if not children:
            # Terminal
            return node.is_winner(self.turn_id)

        # Apply heuristic.
        return self.eval_heuristic(node)


    def compute_best_move(self, node):
        """
        Returns the best next move (in the form of a state) for
        the player whose turn it is (as defined by node.turn).

        Args:
            node: The node on which to branch, i.e. usually the current State.

        Returns: The best successor node for the player whose turn it is.
        """

        best_node = None
        best_gamma = None

        for c in node.successors():
            gamma = self.df_alpha_beta(c, float('-infty'), float('infty'))

            if node.turn == self.turn_id:
                # gamma == alpha; maximize alpha
                if best_node is None or best_gamma < gamma:
                    best_node = c
                    best_gamma = gamma
            else:
                # gamma == beta; minimize beta
                if best_node is None or best_gamma > gamma:
                    best_node = c
                    best_gamma = gamma

        return best_node

    def df_alpha_beta(self, node, alpha, beta):
        """
        Applies alpha beta pruning in a depth limited fashion to the
        game tree.

        Args:
            node: The current node to explore.
            alpha: From the alpha-beta algorithm.
            beta: From the alpha-beta algorithm.

        Returns: The utility value (possibly approximated via an heuristic)
                 of the terminal node of the DFS.
        """

        children = node.successors()

        if not children:
            # Terminal
            return self.utility(node)

        if node.turn == self.turn_id:
            # Maximize self.
            for c in children:
                alpha = max(alpha, self.df_alpha_beta(c, alpha, beta))
                if beta <= alpha:
                    break
            return alpha
        else:
            # Minimize opponent.
            for c in children:
                beta = min(beta, self.df_alpha_beta(c, alpha, beta))
                if beta <= alpha:
                    break
            return beta
