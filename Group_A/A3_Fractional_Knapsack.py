
profit = [60, 100, 120]
weight = [10, 20, 30]

capacity = 50
n = len(profit)

# Calculate profit/weight ratio
ratio = []

for i in range(n):
    ratio.append(profit[i] / weight[i])

# Sort items by ratio
for i in range(n):
    for j in range(i + 1, n):
        if ratio[i] < ratio[j]:
            ratio[i], ratio[j] = ratio[j], ratio[i]
            profit[i], profit[j] = profit[j], profit[i]
            weight[i], weight[j] = weight[j], weight[i]

total_profit = 0

# Select items
for i in range(n):
    if weight[i] <= capacity:
        total_profit += profit[i]
        capacity -= weight[i]
    else:
        total_profit += ratio[i] * capacity
        break

print("Maximum Profit:", total_profit)
