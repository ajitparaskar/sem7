
jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

# Sort jobs by profit in descending order
jobs.sort(key=lambda x: x[2], reverse=True)

# Create time slots
max_deadline = max(job[1] for job in jobs)
slots = [None] * max_deadline

total_profit = 0

# Schedule jobs using greedy method
for job in jobs:
    name, deadline, profit = job

    for i in range(min(deadline, max_deadline) - 1, -1, -1):
        if slots[i] is None:
            slots[i] = name
            total_profit += profit
            break

print("Scheduled Jobs:", slots)
print("Maximum Profit:", total_profit)
