
N = 8

# Take first queen's position
row = int(input("Enter first queen row (1-8): ")) - 1
col = int(input("Enter first queen column (1-8): ")) - 1

board = [-1] * N
board[row] = col

# Check whether queen can be placed safely
def safe(row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True

# Backtracking function
def solve(row):
    if row == N:
        return True

    if row == 0 and board[0] != -1:
        return solve(row + 1)

    for col in range(N):
        if safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False

if solve(0):
    print("Solution:")
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution exists")
