def fibonacci(n):
    a, b = 0, 1
    steps = 0

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
        steps += 1

    print("\nComputational steps:", steps)


n = int(input("Enter number of terms: "))

fibonacci(n)