import random


class EightPuzzle:
    """ Representation of an 8-Puzzle where the default target state is:
            | 1 | 2 | 3 |
            | 4 | 5 | 6 |       The blank square is represented by 0.
            | 7 | 8 |   |
    """
    def __init__(self, initial=(1, 2, 3, 4, 5, 6, 7, 8, 0), goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        self.initial = initial
        self.goal = goal

    """ 
    """
    @staticmethod
    def find_blank_square(state):
        return state.index(0)

    """ Método que retorna las posibles acciones 
    """
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

    def result(self, state, action):
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        return state == self.goal

    def scramble(self, mov=30):
        init = self.initial
        moves = 0

        while moves < mov:
            move = random.choice(self.actions(init))
            init = self.result(init, move)
            self.initial = init
            moves += 1

    def h(self, node):
        return sum(s != g for (s, g) in zip(node.state, self.goal))


def scramble(moves=30):
    puzzle = EightPuzzle()
    puzzle.scramble(moves)
    state = puzzle.initial
    return tuple(state)


def have_solution(state):
    inversion = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                inversion += 1
    return inversion % 2 == 0
