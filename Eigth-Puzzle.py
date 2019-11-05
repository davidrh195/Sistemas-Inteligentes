import sys
from time import time
from Problems.Puzzle import EightPuzzle, scramble, have_solution
from Utils.Search import BFS, DFS, IDS, ASTAR

initial_state = scramble()
# initial_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)
print(initial_state)
option = sys.stdin.readline().strip()

if option.upper() == "BFS":
    start_time = time()
    result = BFS(EightPuzzle(initial_state)).solve() if have_solution(initial_state) else None
    elapsed_time = time() - start_time
    if result is None:
        print("Solution not found")
    else:
        print("You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
            len(result[0])) + " moves:")
        print(list(result[0]), "\n")
        print("Time:", result[1], "nodes")
        print("Space:", result[2], "nodes")
    print("Elapsed time: %0.10f seconds." % elapsed_time)
elif option.upper() == "DFS":
    start_time = time()
    result = DFS(EightPuzzle(initial_state)).solve() if have_solution(initial_state) else None
    elapsed_time = time() - start_time
    if result is None:
        print("Solution not found")
    else:
        print("You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
            len(result[0])) + " moves:")
        print(list(result[0]), "\n")
        print("Time:", result[1], "nodes")
        print("Space:", result[2], "nodes")
    print("Elapsed time: %0.10f seconds." % elapsed_time)
elif option.upper() == "IDS":
    start_time = time()
    result = IDS(EightPuzzle(initial_state)).solve() if have_solution(initial_state) else None
    elapsed_time = time() - start_time
    if result is None:
        print("Solution nit found")
    else:
        print("You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
            len(result[0])) + " moves:")
        print(list(result[0]), "\n")
        print("Time:", result[1], "nodes")
        print("Space:", result[2], "nodes")
    print("Elapsed time: %0.10f seconds." % elapsed_time)
elif option.upper() == "A*" or option.upper() == "A-STAR":
    start_time = time()
    result = ASTAR(EightPuzzle(initial_state)).solve() if have_solution(initial_state) else None
    elapsed_time = time() - start_time
    if result is None:
        print("Solution nit found")
    else:
        print("You have to do " + str(len(result[0])) + " move:" if len(result[0]) == 1 else "You have to do " + str(
            len(result[0])) + " moves:")
        print(list(result[0]), "\n")
        print("Time:", result[1], "nodes")
        print("Space:", result[2], "nodes")
    print("Elapsed time: %0.10f seconds." % elapsed_time)
elif option.upper() == "ALL":
    tries = 20
    bfs_t, bfs_s, dfs_t, dfs_s, ids_t, ids_s, astar_t, astar_s = [0]*8
    bfs_et, dfs_et, ids_et, astar_et = [0.0]*4
    for _ in range(tries):
        initial_state = initial_state if have_solution(initial_state) else scramble()
        start_time = time()
        t, s = BFS(EightPuzzle(initial_state)).solve(False)
        elapsed_time = time() - start_time
        bfs_et += elapsed_time
        bfs_t += t
        bfs_s += s

        start_time = time()
        t, s = DFS(EightPuzzle(initial_state)).solve(False)
        elapsed_time = time() - start_time
        dfs_et += elapsed_time
        dfs_t += t
        dfs_s += s

        start_time = time()
        t, s = IDS(EightPuzzle(initial_state)).solve(False)
        elapsed_time = time() - start_time
        ids_et += elapsed_time
        ids_t += t
        ids_s += s

        initial_state = scramble()
    print("=======================================\nBFS")
    print("Time:", bfs_t/tries)
    print("Space:", bfs_s/tries)
    print("Elapsed time: %0.10f seconds." % (bfs_et/tries))

    print("=======================================\nDFS")
    print("Time:", dfs_t/tries)
    print("Space:", dfs_s/tries)
    print("Elapsed time: %0.10f seconds." % (dfs_et/tries))

    print("=======================================\nIDS")
    print("Time:", ids_t/tries)
    print("Space:", ids_s/tries)
    print("Elapsed time: %0.10f seconds." % (ids_et/tries))
else:
    print("Opcion no valida")
