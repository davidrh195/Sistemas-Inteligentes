from collections import deque
import heapq


class Node:

    def __init__(self, state, parent=None, prevAcc=None, path_cost=1):
        self.state = state
        self.parent = parent
        self.prevAcc = prevAcc
        self.depth = 0
        self.path_cost = path_cost
        if parent:
            self.depth = parent.depth + 1

    def __lt__(self, node):
        return self.state < node.state

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(self.state)


class Queue(deque):

    def isEmpty(self):
        return len(self) == 0

    def add(self, item):
        self.append(item)

    def discard(self):
        if self:
            return self.popleft()
        else:
            raise Exception('Trying to pop from empty Queue.')

    def size(self):
        return len(self)


class Stack(deque):

    def isEmpty(self):
        return len(self) == 0

    def add(self, item):
        self.append(item)

    def discard(self):
        if self:
            return self.pop()
        else:
            raise Exception('Trying to pop from empty Stack.')

    def size(self):
        return len(self)


class PriorityQueue:

    def __init__(self, order='min', f=lambda x: x):
        self.heap = []
        if order == 'min':
            self.f = f
        elif order == 'max':
            self.f = lambda x: -f(x)
        else:
            raise ValueError("order must be either 'min' or 'max'.")

    def __contains__(self, key):
        return any([item == key for _, item in self.heap])

    def __getitem__(self, key):
        for value, item in self.heap:
            if item == key:
                return value
        raise KeyError(str(key) + " is not in the priority queue")

    def __delitem__(self, key):
        try:
            del self.heap[[item == key for _, item in self.heap].index(True)]
        except ValueError:
            raise KeyError(str(key) + " is not in the priority queue")
        heapq.heapify(self.heap)

    def isEmpty(self):
        return len(self.heap) == 0

    def add(self, item):
        heapq.heappush(self.heap, (self.f(item), item))

    def extend(self, items):
        for item in items:
            self.append(item)

    def discard(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    def size(self):
        return len(self.heap)
