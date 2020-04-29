import random
import sys
from collections import deque


class Agent:
    def __init__(self):
        self.ans = self.findPossAns()
        self.guess = ""

    """ Method that find all the possible answers and returned them in a list. The 'valid' variable verifies that each
        digit on the possible answer only appears once.
    """
    @staticmethod
    def findPossAns():
        ans = deque()
        for x in range(122, 9880):
            x = "0"+str(x) if x < 1000 else str(x)
            valid = 1 == x.count(x[0]) == x.count(x[1]) == x.count(x[2]) == x.count(x[3])
            if valid:
                ans.append(x)
        return ans

    """ Method that decrease the number of the possible answers by remove them depending of the number of "Picas" and
        "Fijas" of the guess.
    """
    def decrease(self, picas, fijas):
        index = 0
        while index < len(self.ans):
            if self.remove(self.ans[index], picas, fijas):
                self.ans.remove(self.ans[index])
            else:
                index += 1

    """ This method determine if a possible answer has to be remove or not. That depends if the number of "Picas" and
        "Fijas" of the guess are the same of the number of "Picas" and "Fijas" of the possible answer, if the are the
        same that number could be the answer.
    """
    def remove(self, poss_ans, picas, fijas):
        nPicas = 0
        nFijas = 0
        guess = self.guess
        for i in range(len(guess)):
            if poss_ans.count(guess[i]):
                k = poss_ans.index(guess[i])
                nFijas = nFijas+1 if k == i else nFijas
                nPicas = nPicas+1 if k != i else nPicas
        return not (nPicas == picas and nFijas == fijas)

    """ This method will act as the Agent sensors, the sensors receive a perception from the Environment and return the
        respective action. In this case the perception could be the word START or the number od "Picas" and "Fijas" of
        the previous guess.
    """
    def sensors(self, perception):
        if perception == "START":
            self.guess = random.choice(self.ans)
            return self.guess
        else:
            if int(perception[1]) == 4:
                return "STOP"
            # If the previous guess is not the answer(the number of "Fijas" is not 4), the list of possible answers
            # will be decreased on base of the number of "Picas" and "Fijas" and then will be choose the next guess
            self.decrease(int(perception[0]), int(perception[1]))
            if len(self.ans) == 0:
                return "TRAP"
            self.guess = random.choice(self.ans)
            return self.guess


class Environment:
    def __init__(self, agent):
        self.tried = 0
        self.agent = agent

    """ The game starts with sending a perception to the agent, witch is responsible to returning the respective action.
        This process continues until the agent return a "STOP"(if it was capable to find the answer), or "TRAP"(if there
        was some cheating)
    """
    def start(self):
        action = self.agent.sensors(self.perception())
        while action != "STOP" and action != "TRAP":
            print("Turn:", self.tried)
            print(action)
            action = self.agent.sensors(self.perception())
        print("\nYOU CHEATED" if action == "TRAP" else "\nGOOD GAME")

    """ This method will be the environment perceptions, the environment has a variable that counts the number of tries
        of the Agent, when this variable is 0, that means that the is not started yet so the environment says to the
        agent "START", and when the game is already started, the environment asks to the user the number of "Picas" and
        "Fijas" of the guess to send them to the agent.
    """
    def perception(self):
        if self.tried == 0:
            self.tried += 1
            return "START"
        else:
            self.tried += 1
            print("P", "F")
            return sys.stdin.readline().strip().split(" ")
