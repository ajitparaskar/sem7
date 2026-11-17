
profit = [60, 100, 120]
weight = [10, 20, 30]

capacity = 50
n = len(profit)

# Create DP table
dp = [[0 for j in range(capacity + 1)]
      for i in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for j in range(1, capacity + 1):

        if weight[i - 1] <= j:
            dp[i][j] = max(
                profit[i - 1] + dp[i - 1][j - weight[i - 1]],
                dp[i - 1][j]
            )
        else:
            dp[i][j] = dp[i - 1][j]

# Print maximum profit
print("Maximum Profit:", dp[n][capacity])
