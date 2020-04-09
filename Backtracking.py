import time

""" This is a backracking-based algorithm solving the n-queens problem """

""" The backtracking algorithm uses incremental formulation to solve the problem(starting with 0 queens on board).
    However, we need a place to store the queens in our array in a way that doesn't affect our algorithm.
    So, we use the N'th position of array as it is not used to store the queens. In this way, we consider a queen beeing in index N as a queen not placed on board. """
def nqueens(N):                                                         # Calls successor function to solve the problem for N queens
    successorFunction(list(N for i in range(N)), 0, N)                  # We put all our queens on N index(not placed on board)

""" hits function: Finds how many queens threaten a specific queen placed on column col"""
def hits(board, N, col, row):
    total = 0                                                                             # Start: 0 threats
    for i in range(N):                                                                    # Search all columns
        if i == col or board[i] == N:                                                     # i == col: We are looking at the current queen - board[i] == N: The queen is not placed on board
            continue                                                                      # No threats
        if board[i] == row or abs(i - col) == abs(board[i] - row):                        # board[i] == row: queen on same row found - abs(i - col) == abs(board[i] - row): queen found diagonally
            total += 1                                                                    # Threat found! Increment queen's threatens
    return total                                                                          # Total threats


""" successorFunction function: The successor function of our algorithm. Performs all necessart actions to solve the problem"""
def successorFunction(board, col, N):
    global flag                                                                           # This flag is used to stop the algorithm when a solution is found. We made another implementation to find all possible solutions.
    if flag == 0:                                                                         # flag == 0: No solution is found yet
        if col >= N:                                                                      # col >= N: We surpassed our columns without finding solution - Something went wrong
            return                                                                        # Stop program

        for i in range(N):                                                                # For each row
            if hits(board, N, col, i) == 0:                                               # If no threats are found in this block - we are safe to put the queen
                board[col] = i                                                            # Place queen
                if col == N - 1:                                                          # If we just placed the queen while beeing in the last column, we found a solution!
                    print(board)                                                          # Print our solution
                    flag = 1                                                              # Flag as solution found!
                    return                                                                # Stop program
                successorFunction(board, col + 1, N)                                      # We are not in the last column but we found a safe block to put our queen. We now use recursion to find a place for our next queen
                board[col] = N                                                            # If we reach this instruction, it means that we didn't find a solution, so we need to put the previous queen on the next safe block. We remove this queen from board.

    else:                                                                                 # We already found a solution.
        return                                                                            # Stop program


def backtrackingOneMain(startingPoint, endingPoint, step,repetitions):                    # Main function
    global flag                                                                           # Declare flag( explained on successorFunction) as a global variable
    executionTimes = []                                                                   # Array holding time needed to find a solution for each N
    for i in range(startingPoint, endingPoint, step):                                     # Solve problem for startingPoint-queens up to endingPoint-queens with a step
        totalExecTime = 0                                                                 # Declare starting time as zero each time we solve the problem
        for j in range(repetitions):                                                      # Repeats the algorithm repetitions times
            flag = 0                                                                      # No solution is found at start
            start_time = time.time()                                                      # Declare start time
            nqueens(i)                                                                    # Call to solve problem for current queens
            execTime = time.time() - start_time                                           # Count time needed to find solution
            totalExecTime = totalExecTime + execTime                                      # Count total execution time for all repetitions
            print("%d queens solution found in %s seconds" % (i, execTime))               # Print execution time
        executionTimes.append(totalExecTime/repetitions)                                  # Put execution time in executionTimes array

    print(executionTimes)                                                                 # Print all execution times
    return executionTimes                                                                 # Return all execution times
