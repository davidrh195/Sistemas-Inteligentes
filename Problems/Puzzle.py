import random


class EightPuzzle:
    """ Representation of an 8-Puzzle where the default target state is:
            | 1 | 2 | 3 |
            | 4 | 5 | 6 |       The blank square is represented by 0.
            | 7 | 8 |   |

        The "mem" matrix represents the minimum number of moves that a tile has to do to reach their target position.
        For example:
            | 4 | 1 | 3 |   The '4' tile is in 0 position so it has to do one move "DOWN", so in the mem matrix, in the
            | 2 |   | 8 |   row of the tile '4' an in column of position '0', will be the number one.
            | 7 | 6 | 5 |
    """
    def __init__(self, initial=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        self.goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        self.initial = initial
        # position   0  1  2  3  4  5  6  7  8
        self.mem = [[0, 0, 0, 0, 0, 0, 0, 0, 0],# blank
                    [0, 1, 2, 1, 2, 3, 2, 3, 4],#   1
                    [1, 0, 1, 2, 1, 2, 3, 2, 3],#   2
                    [2, 1, 0, 3, 2, 1, 4, 3, 2],#   3
                    [1, 2, 3, 0, 1, 2, 1, 2, 3],#   4
                    [2, 1, 2, 1, 0, 1, 2, 1, 2],#   5
                    [3, 2, 1, 2, 1, 0, 3, 2, 1],#   6
                    [2, 3, 4, 1, 2, 3, 0, 1, 2],#   7
                    [3, 2, 3, 2, 1, 2, 1, 0, 1]]#   8
                                                # Tiles

    """ Method that returns the index of the blank square of any state. """
    @staticmethod
    def find_blank_square(state):
        return state.index(0)

    """ Method that returns the list of possible actions depending of the position of the blank square. """
    def actions(self, state):
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')

        return possible_actions

    """ This method is responsible for applying the action to the current state to generate the new state. """
    def result(self, state, action):
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    """ Method that verifies if the current state is the goal. """
    def goal_test(self, state):
        return state == self.goal

    """ This method generate a resolvable random state, applying actions to the target state as many as the mov variable
        dictates.
    """
    def scramble(self, mov=30):
        init = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        moves = 0

        while moves < mov:
            move = random.choice(self.actions(init))
            init = self.result(init, move)
            self.initial = init
            moves += 1

    """ Method that verifies if the initial state is resolvable. """
    def has_solution(self):
        state = self.initial
        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1
        return inversion % 2 == 0

    """ This method has the problem heuristics. """
    def h(self, node):
        # Misplace tiles
        # return sum(s != g and s != 0 for (s, g) in zip(node.state, self.goal))
        # Minimum distance from the actual position of the tile, and the target position
        return sum(self.mem[node.state[i]][i] for i in range(len(node.state)))
