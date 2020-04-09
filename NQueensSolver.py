import Backtracking
import BacktrackAll
import MinConflicts
import matplotlib.pyplot as plt

if __name__ == '__main__':																				#python main

    while True:																							#menu...trivial programming
        print("N-Queens solver")
        print("Choose algorithm to test:")
        print("\t Press 1 for Minimum Conflicts local search algorithm")
        print("\t Press 2 for Backtacking constraint satisfaction algorithm (finds all solutions)")
        print("\t Press 3 for Backtacking constraint satisfaction algorithm (finds one solutions)")
        answer = int(input("Your answer: "))

        startingPoint = int(input("Enter starting chessboard size: "))
        endingPoint = int(input("Enter ending chessboard size: "))
        step = int(input("Enter step value: "))

        repetitions = int(input("Enter repetitions for each value of n: "))

        if answer == 1:																					# algorithms return the data to be plotted
            execTimeList = MinConflicts.minConflictsMain(startingPoint, endingPoint, step, repetitions)
        elif answer == 2:
            execTimeList = BacktrackAll.backtrackingAllMain(startingPoint, endingPoint, step, repetitions)
        elif answer == 3:
            execTimeList = Backtracking.backtrackingOneMain(startingPoint, endingPoint, step, repetitions)

        plt.plot(list(range(startingPoint, endingPoint, step)), execTimeList)							# data is being plotted
        if answer == 1:
            plt.title("N-Queens from %d to %d with %d repetitions per n\nUsing MinConflicts" % (startingPoint, endingPoint, 10))
        elif answer == 2:
            plt.title("N-Queens from %d to %d with %d repetitions per n\nUsing Backtracking(all solutions)" % (startingPoint, endingPoint, repetitions))
        elif answer == 3:
            plt.title("N-Queens from %d to %d with %d repetitions per n\nUsing Backtracking(one solution)" % (startingPoint, endingPoint, repetitions))

        plt.xlabel("N")
        plt.ylabel("time in seconds")
        plt.show()

        exitAnswer = int(input('\n\nPress 0 to exit, 1-9 to continue\n\n'))
        if exitAnswer == 0:
            break
