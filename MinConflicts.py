# A solution to N-Queens using the Min-Conflicts local search algorithm
import time
import random

""" This is a minimum conflicts based algorithm solving the n-queens problem """

""" The minimum conflicts algorithm uses full-state formulation to solve the problem(starts with all queens on board).
This algorithm formulates board in many states using randomness while taking threats into consideration. """
def nqueens(N):                                                                         # Calls successor function to solve the problem for N queens
    print(successorFunction(list(range(N)), N))                                         # We put all our queens diagonally so that each threatens each other


""" successorFunction function: The successor function of our algorithm. Performs all necessary actions to solve the problem"""
def successorFunction(board, N, iters=20000):                                           # We do a lot of iterations in order to get our board to as many different states as possible
    def random_pos(conflicts, filter):                                                  # random_pos function
        return random.choice([i for i in range(N) if filter(conflicts[i])])             # Picks a random number(0-(N-1)) for conflicting queens while filtering results. This number will be used as index to place queens

    for k in range(iters):                                                              # For all iterations(board states)
        confs = find_conflicts(board, N)                                                # Find conflicts for each queen on board - confs is an array holding each queen's threats
        if sum(confs) == 0:                                                             # No threats on our board - Solution found!
            return board                                                                  # Return the solution
        col = random_pos(confs, lambda elt: elt > 0)                                    # Select a random queen from those conflicting(threatened). The filter is applied using a lambda function that keeps only the queens conflictiong
        vconfs = [hits(board, N, col, row) for row in range(N)]                         # We use array vconfs to hold conflict number in each row possible to put our current queen
        board[col] = random_pos(vconfs, lambda elt: elt == min(vconfs))                 # We put our queen in a row having minimum conflicts. In case we have many rows with the same number of conflicts, we pick a row randomly using random_pos function. Lamda expression is used as a filter to keep minimum conflicted rows.
    raise Exception("Incomplete solution: try more iterations.")                        # If we didn't return, it means that the states the algorithm formulated haven't found a solution. - Maybe more iterations are needed, but be careful: More iterations will slow down the algorithm.


""" find_conflicts function: Find conflicts(threats) for each queen on board"""
def find_conflicts(board, N):
    return [hits(board, N, col, board[col]) for col in range(N)]                        # Calls hits function for each queen. Returns an array with conflicts for each queen

""" hits function: Finds how many queens threaten a specific queen placed on column col"""
def hits(board, N, col, row):
    total = 0                                                                           # Start: 0 threats
    for i in range(N):                                                                  # Search all columns
        if i == col:                                                                    # i == col: We are looking at the current queen
            continue                                                                    # Not a threat
        if board[i] == row or abs(i - col) == abs(board[i] - row):                      # board[i] == row: queen on same row found - abs(i - col) == abs(board[i] - row): queen found diagonally
            total += 1                                                                  # Threat found! Increment queen's threatens
    return total                                                                        # Total threats


def minConflictsMain(startingPoint, endingPoint, step, repetitions):                    # Main function
    executionTimes = []                                                                 # Array holding time needed to find a solution for each N
    for i in range(startingPoint, endingPoint, step):                                   # Solve problem for startingPoint-queens up to endingPoint-queens with a step
        totalExecTime = 0                                                               # Declare starting time as zero each time we solve the problem
        for j in range(repetitions):                                                    # Repeats the algorithm repetitions times
            start_time = time.time()                                                    # Declare start time
            nqueens(i)                                                                  # Call to solve problem for current queens
            execTime = time.time() - start_time                                         # Count time needed to find solution
            totalExecTime = totalExecTime + execTime                                    # Count total execution time for all repetitions
            print("%d queens solution found in %s seconds" % (i, execTime))             # Print execution time
        executionTimes.append(totalExecTime/repetitions)                                # Put execution time in executionTimes array

    print(executionTimes)                                                               # Print all execution times
    return executionTimes                                                               # Return all execution times

# minConflictsMain()