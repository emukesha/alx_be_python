n = int(input("Enter the size of the pattern: "))
counter = 1
while counter <= n:
    for i in range(n):
        print("*", end="")
    print()
    counter += 1