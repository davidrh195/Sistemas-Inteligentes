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
#puzzle = EightPuzzle((0, 1, 2, 3, 4, 5, 6, 7, 8))

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
            print(
                "You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
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
            print(
                "You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
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
            print(
                "You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
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
            print(
                "You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
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
            print(
                "You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
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
            print(
                "You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
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
        elif i.upper().find("DLS") == 0:
            new_option = i.upper().split("-")
            if len(new_option) < 2:
                print(colored("For DLS no limit parameter was found", "red"))
            else:
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
    av_time = np.zeros(len(option))
    num_of_solution_not_found = np.zeros(len(option))
    for _ in range(tries):
        puzzle.scramble(14)
        for i in range(len(option)):
            if option[i].upper() == "BFS":
                start_time = time()
                answer = BFS(puzzle).solve(False)
                elapsed_time = time() - start_time
                av_time[i] += elapsed_time
                time_complex[i] += answer[0] if answer is not None else 0
                space_complex[i] += answer[1] if answer is not None else 0
                num_of_solution_not_found[i] += 1 if answer is None else 0
            elif option[i].upper() == "DFS":
                start_time = time()
                answer = DFS(puzzle).solve(False)
                elapsed_time = time() - start_time
                av_time[i] += elapsed_time
                time_complex[i] += answer[0] if answer is not None else 0
                space_complex[i] += answer[1] if answer is not None else 0
                num_of_solution_not_found[i] += 1 if answer is None else 0
            elif option[i].upper().find("DLS") == 0:
                new_option = option[i].upper().split("-")
                limit = int(new_option[1])
                start_time = time()
                answer = DLS(puzzle, limit).solve(False)
                elapsed_time = time() - start_time
                av_time[i] += elapsed_time
                time_complex[i] += answer[0] if answer is not None else 0
                space_complex[i] += answer[1] if answer is not None else 0
                num_of_solution_not_found[i] += 1 if answer is None else 0
            elif option[i].upper() == "IDS":
                start_time = time()
                answer = IDS(puzzle).solve(False)
                elapsed_time = time() - start_time
                av_time[i] += elapsed_time
                time_complex[i] += answer[0] if answer is not None else 0
                space_complex[i] += answer[1] if answer is not None else 0
                num_of_solution_not_found[i] += 1 if answer is None else 0
            elif option[i] == "A*(Misplaced)":
                puzzle.setHeuristic("misplace")
                start_time = time()
                answer = ASTAR(puzzle).solve(False)
                elapsed_time = time() - start_time
                av_time[i] += elapsed_time
                time_complex[i] += answer[0] if answer is not None else 0
                space_complex[i] += answer[1] if answer is not None else 0
                num_of_solution_not_found[i] += 1 if answer is None else 0
            elif option[i] == "A*(Manhattan)":
                puzzle.setHeuristic("manhattan")
                start_time = time()
                answer = ASTAR(puzzle).solve(False)
                elapsed_time = time() - start_time
                av_time[i] += elapsed_time
                time_complex[i] += answer[0] if answer is not None else 0
                space_complex[i] += answer[1] if answer is not None else 0
                num_of_solution_not_found[i] += 1 if answer is None else 0

    average_expanded_nodes = np.zeros(len(option))
    average_length_nodes = np.zeros(len(option))
    average_time = np.zeros(len(option))
    for i in range(len(option)):
        average_expanded_nodes[i] = "----" if num_of_solution_not_found[i] == tries \
            else time_complex[i] // (tries - num_of_solution_not_found[i])
        average_length_nodes[i] = "----" if num_of_solution_not_found[i] == tries \
            else space_complex[i] // (tries - num_of_solution_not_found[i])
        average_time[i] = "----" if num_of_solution_not_found[i] == tries \
            else av_time[i] / tries

    d1 = pd.DataFrame({'Search': option,
                       'Expanded nodes': average_expanded_nodes,
                       'Maximum length of the list': average_length_nodes})

    d2 = pd.DataFrame({'Search': option,
                       'Average time(sec)': average_time,
                       'N°. Solution not found': num_of_solution_not_found})

    print("Number of tries: %d \n" % tries)
    print(d1, "\n")
    print(d2)
