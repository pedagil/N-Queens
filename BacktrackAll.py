import copy
import time


def nqueens(N):
    successorFunction(list(N for i in range(N)), 0, N)


def hits(board, N, col, row):
    total = 0
    for i in range(N):
        if i == col or board[i] == N:
            continue
        if board[i] == row or abs(i - col) == abs(board[i] - row):
            total += 1
    return total


def successorFunction(board, col, N):
    """Use backtracking to find all solutions"""
    global solutions
    # base case
    if col >= N:
        return

    for i in range(N):
        if hits(board, N, col, i) == 0:
            board[col] = i
            if col == N - 1:
                # print(board)
                solutions = solutions + 1
                add_solution(board)
                board[col] = N
                return
            successorFunction(board, col + 1, N)
            # backtrack
            board[col] = N


def add_solution(board):
    """Saves the board state to the global variable 'solutions'"""
    saved_board = copy.deepcopy(board)
    allSolutions.append(saved_board)


def backtrackingAllMain(startingPoint, endingPoint, step, repetitions):

    executionTimes = []
    global solutions
    global allSolutions
    allSolutions = []

    for i in range(startingPoint, endingPoint, step):
        totalExecTime = 0
        for j in range(repetitions):
            solutions = 0
            start_time = time.time()
            nqueens(i)
            execTime = time.time() - start_time
            totalExecTime = totalExecTime + execTime
            print("%d queens has %d solutions found in %s seconds" % (i, solutions, execTime))
        executionTimes.append(totalExecTime/repetitions)

    print(executionTimes)
    print(allSolutions)
    return executionTimes


#backtrackingAllMain()