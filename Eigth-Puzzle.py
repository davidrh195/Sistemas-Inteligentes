import sys, numpy as np, pandas as pd
from time import time
from termcolor import colored

from Problems.Puzzle import EightPuzzle
from Utils.Search import BFS, DFS, DLS, IDS, ASTAR

print("What kind of searches do you want to apply:")
print("(options: bfs, dfs, dls-n, ids, a*)")
print(colored("* The n in dls-n, is the limit of the Depth Limited Search", "blue"))
print(colored("* If pass more than 1 search, will apply all and returns", "blue"))
print(colored("  a comparison between them", "blue"))
option = sys.stdin.readline().strip().split(" ")
puzzle = EightPuzzle()
# puzzle = EightPuzzle((0, 1, 2, 3, 4, 5, 6, 7, 8))

if len(option) == 1:
    puzzle.scramble(14)
    print("Initial state:\n", puzzle.initial)
    if option[0].upper() == "BFS":
        start_time = time()
        result = BFS(puzzle).solve() if puzzle.has_solution() else None
        elapsed_time = time() - start_time
        if result is None:
            print(colored("Solution not found", "red"))
        else:
            print("##############################################")
            print("You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
                len(result[0])) + " moves:")
            print(list(result[0]), "\n")
            d = pd.DataFrame({'Expanded nodes': [result[1]], 'Maximum length of the list': [result[2]]})
            print(d, "\n")
        print("Elapsed time: %0.10f seconds." % elapsed_time)
    elif option[0].upper() == "DFS":
        start_time = time()
        result = DFS(puzzle).solve() if puzzle.has_solution() else None
        elapsed_time = time() - start_time
        if result is None:
            print(colored("Solution not found", "red"))
        else:
            print("##############################################")
            print("You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
                len(result[0])) + " moves:")
            print(list(result[0]), "\n")
            d = pd.DataFrame({'Expanded nodes': [result[1]], 'Maximum length of the list': [result[2]]})
            print(d, "\n")
        print("Elapsed time: %0.10f seconds." % elapsed_time)
    elif option[0].upper().find("DLS") == 0:
        new_option = option[0].upper().split("-")
        if len(new_option) < 2:
            print(colored("No limit parameter was found", "red"))
            sys.exit()
        limit = int(new_option[1])
        start_time = time()
        result = DLS(puzzle, limit).solve() if puzzle.has_solution() else None
        elapsed_time = time() - start_time
        if result is None:
            print(colored("Solution not found at depth %d, try with a higher limit" % limit, "red"))
        else:
            print("##############################################")
            print("You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
                len(result[0])) + " moves:")
            print(list(result[0]), "\n")
            d = pd.DataFrame({'Expanded nodes': [result[1]], 'Maximum length of the list': [result[2]]})
            print(d, "\n")
        print("Elapsed time: %0.10f seconds." % elapsed_time)
    elif option[0].upper() == "IDS":
        start_time = time()
        result = IDS(puzzle).solve() if puzzle.has_solution() else None
        elapsed_time = time() - start_time
        if result is None:
            print(colored("Solution not found", "red"))
        else:
            print("##############################################")
            print("You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
                len(result[0])) + " moves:")
            print(list(result[0]), "\n")
            d = pd.DataFrame({'Expanded nodes': [result[1]], 'Maximum length of the list': [result[2]]})
            print(d, "\n")
        print("Elapsed time: %0.10f seconds." % elapsed_time)
    elif option[0].upper() == "A*":
        print("##############################################")
        print("Misplace Tiles")
        puzzle.setHeuristic("misplace")
        start_time = time()
        result = ASTAR(puzzle).solve() if puzzle.has_solution() else None
        elapsed_time = time() - start_time
        if result is None:
            print(colored("Solution not found", "red"))
        else:
            print("You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
                len(result[0])) + " moves:")
            print(list(result[0]), "\n")
            d = pd.DataFrame({'Expanded nodes': [result[1]], 'Maximum length of the list': [result[2]]})
            print(d, "\n")
        print("Elapsed time: %0.10f seconds." % elapsed_time)

        print("##############################################")
        print("Manhattan")
        puzzle.setHeuristic("manhattan")
        start_time = time()
        result = ASTAR(puzzle).solve() if puzzle.has_solution() else None
        elapsed_time = time() - start_time
        if result is None:
            print(colored("Solution not found", "red"))
        else:
            print("You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
                len(result[0])) + " moves:")
            print(list(result[0]), "\n")
            d = pd.DataFrame({'Expanded nodes': [result[1]], 'Maximum length of the list': [result[2]]})
            print(d, "\n")
        print("Elapsed time: %0.10f seconds." % elapsed_time)
    else:
        print(colored("%s search not found" % option[0], "red"))
else:
    aux = []
    for i in option:
        if i.upper() == "BFS" or i.upper() == "DFS" or i.upper() == "IDS":
            aux.append(i)
        elif i.upper() == "A*":
            aux.append("A*(Misplaced)")
            aux.append("A*(Manhattan)")
        else:
            print(colored("%s search not found" % i, "red"))
    option = aux

    tries = 30
    time_complex = np.zeros(len(option))
    space_complex = np.zeros(len(option))
    average_time = np.zeros(len(option))
    for _ in range(tries):
        puzzle.scramble(14)
        for i in range(len(option)):
            if option[i].upper() == "BFS":
                start_time = time()
                t, s = BFS(puzzle).solve(False)
                elapsed_time = time() - start_time
                average_time[i] += elapsed_time
                time_complex[i] += t
                space_complex[i] += s
            elif option[i].upper() == "DFS":
                start_time = time()
                t, s = DFS(puzzle).solve(False)
                elapsed_time = time() - start_time
                average_time[i] += elapsed_time
                time_complex[i] += t
                space_complex[i] += s
            elif option[i].upper() == "IDS":
                start_time = time()
                t, s = IDS(puzzle).solve(False)
                elapsed_time = time() - start_time
                average_time[i] += elapsed_time
                time_complex[i] += t
                space_complex[i] += s
            elif option[i] == "A*(Misplaced)":
                puzzle.setHeuristic("misplace")
                start_time = time()
                t, s = ASTAR(puzzle).solve(False)
                elapsed_time = time() - start_time
                average_time[i] += elapsed_time
                time_complex[i] += t
                space_complex[i] += s
            elif option[i] == "A*(Manhattan)":
                puzzle.setHeuristic("manhattan")
                start_time = time()
                t, s = ASTAR(puzzle).solve(False)
                elapsed_time = time() - start_time
                average_time[i] += elapsed_time
                time_complex[i] += t
                space_complex[i] += s

    d = pd.DataFrame({'Search': option, 'Expanded nodes': time_complex//tries,
                      'Maximum length of the list': space_complex//tries, 'Average time(sec)': average_time/tries})
    print("Number of tries: %d \n" % tries)
    print(d)
