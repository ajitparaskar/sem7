n = 5
r = 2

dp = [[0 for j in range(r + 1)]
      for i in range(n + 1)]

for i in range(n + 1):
    for j in range(min(i, r) + 1):

        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print("Binomial Coefficient:", dp[n][r])