# A1

def find_conflicts(arr, N):
    return [hits(arr, N, col, arr[col]) for col in range(N)]


def hits(arr, N, col, row):
    total = 0
    for i in range(N):
        if i == col:
            continue
        if arr[i] == row or abs(i - col) == abs(arr[i] - row):
            total += 1
    return total


def findTotalConflicts(arr):
    return sum(find_conflicts(arr, len(arr)))


print(findTotalConflicts([2, 3, 2, 6, 6, 0, 1, 3]))
