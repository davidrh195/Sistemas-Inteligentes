import sys
from collections import deque
from Utils.Collections import Node, Stack, Queue, PriorityQueue

sys.setrecursionlimit(1000000000)


class BFS:
    def __init__(self, problem):
        self.problem = problem
        self.space = 0
        self.time = 0

    def solve(self, full=True):
        ans = self.search()
        if ans is None:
            return None
        else:
            if full:
                path = deque()
                while ans.parent is not None:
                    path.appendleft(ans.prevAcc)
                    ans = ans.parent
                return [path, self.time, self.space]
            else:
                return [self.time, self.space]

    def search(self):
        queue = Queue()
        visited = set()
        root = Node(self.problem.initial)
        queue.add(root)

        while not queue.isEmpty():
            self.space = queue.size() if queue.size() > self.space else self.space
            node = queue.discard()
            if self.problem.goal_test(node.state):
                return node
            visited.add(node.state)
            self.time = len(visited) if len(visited) > self.time else self.time
            children = self.expand(node)
            aux = deque()
            for child in children:
                if child.state not in visited and child not in queue:
                    if self.problem.goal_test(child.state):
                        aux.append(child)
                    else:
                        aux.appendleft(child)
            a = len(aux)
            for x in range(a):
                queue.add(aux.pop())

        return None

    def expand(self, node):
        children = []
        for action in self.problem.actions(node.state):
            new_state = self.problem.result(node.state, action)
            children.append(Node(new_state, node, action))
        return children


class DFS:
    def __init__(self, problem, limit=float('inf')):
        self.problem = problem
        self.space = 0
        self.time = 0
        self.limit = limit

    def solve(self, full=True):
        ans = self.search()
        if ans is None:
            return None
        else:
            if full:
                path = deque()
                while ans.parent is not None:
                    path.appendleft(ans.prevAcc)
                    ans = ans.parent
                return [path, self.time, self.space]
            else:
                return [self.time, self.space]

    def search(self):
        stack = Stack()
        visited = set()
        root = Node(self.problem.initial)
        stack.add(root)

        while not stack.isEmpty():
            self.space = stack.size() if stack.size() > self.space else self.space
            node = stack.discard()
            if self.problem.goal_test(node.state):
                return node
            visited.add(node.state)
            self.time = len(visited) if len(visited) > self.time else self.time
            children = self.expand(node)
            aux = deque()
            for child in children:
                if child.state not in visited and child not in stack:
                    if self.problem.goal_test(child.state):
                        aux.append(child)
                    else:
                        aux.appendleft(child)
            a = len(aux)
            for x in range(a):
                stack.add(aux.popleft())

        return None

    def expand(self, node):
        children = []
        if node.depth < self.limit:
            for action in self.problem.actions(node.state):
                new_state = self.problem.result(node.state, action)
                children.append(Node(new_state, node, action))
        return children


class IDS:
    def __init__(self, problem):
        self.problem = problem

    def solve(self, full=True):
        for limit in range(sys.maxsize):
            ans = DFS(self.problem, limit).solve(full)
            if ans is not None:
                return ans
        return None


class ASTAR:
    def __init__(self, problem):
        self.problem = problem
        self.space = 0
        self.time = 0
        self.h = problem.h

    def solve(self, full=True):
        ans = self.search()
        if ans is None:
            return None
        else:
            if full:
                path = deque()
                while ans.parent is not None:
                    path.appendleft(ans.prevAcc)
                    ans = ans.parent
                return [path, self.time, self.space]
            else:
                return [self.time, self.space]

    def search(self):
        p_queue = PriorityQueue("min", lambda n: n.path_cost + self.h(n))
        visited = set()
        root = Node(self.problem.initial)
        p_queue.add(root)

        while not p_queue.isEmpty():
            self.space = p_queue.size() if p_queue.size() > self.space else self.space
            node = p_queue.discard()
            if self.problem.goal_test(node.state):
                return node
            visited.add(node.state)
            self.time = len(visited) if len(visited) > self.time else self.time
            children = self.expand(node)
            for child in children:
                if child.state not in visited and child not in p_queue:
                    p_queue.add(child)

        return None

    def expand(self, node):
        children = []
        for action in self.problem.actions(node.state):
            new_state = self.problem.result(node.state, action)
            children.append(Node(new_state, node, action))
        return children
