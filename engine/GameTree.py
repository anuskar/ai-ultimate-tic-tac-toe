"""
The 2-player game tree via a depth limited heuristic based MinMax.
"""
class GameTree:
    def __init__(self, initial_state, opponent_first=False):
        self.current = initial_state
        self.custom_heuristic = None

        self.turn_id = initial_state.turn
        if opponent_first:
            self.turn_id = 1 - initial_state.turn

        self.alpha = float('-infty')
        self.beta = float('infty')

    def prompt_opponent(self):
        pass

    def dictate_move(self, state):
        print(state)

    def play(self, custom_heuristic = None):
        self.custom_heuristic = custom_heuristic

        while True:
            children = self.current.successors()
            if children is None:
                # If we reach a terminal node, then game is over.
                # Return True if we win.
                return self.current.turn == self.turn_id

            # Opponents turn.
            if self.current.turn != self.turn_id:
                # Keep asking for their move until a valid move is made.
                opponents_move = None
                while opponents_move not in children:
                    opponents_move = self.prompt_opponent()

                self.current = opponents_move
                continue

            # Our turn.
            our_move = self.compute_best_move(self.current, children)

            # Tell opponent what we are doing.
            self.dictate_move(our_move)

            self.current = our_move


    def eval_heuristic(self, node):
        if self.custom_heuristic:
            return self.custom_heuristic(self.turn_id, node)

        # Otherwise use some default heuristic.
        return 0

    def utility(self, node):
        children = node.successors()
        if not children:
            # Terminal
            return node.is_winner(self.turn_id)

        # Apply heuristic.
        return self.eval_heuristic(node)

    """
    Returns the best next move (in the form of a state) for
    the player whose turn it is (as defined by node.turn).
    """
    def compute_best_move(self, node):
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
