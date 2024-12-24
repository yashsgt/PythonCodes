def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive step: sum of the two preceding numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_numbers(count):
    for i in range(count):
        print(fibonacci(i), end=" ")

# Input from the user
n = int(input("Enter the number of Fibonacci numbers to print: "))
print_fibonacci_numbers(n)


    