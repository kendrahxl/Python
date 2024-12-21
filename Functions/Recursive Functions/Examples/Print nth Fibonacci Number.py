### Return nth Fibonacci number ###

def fibonacci(n):
    if n < 0:
        return ("Input must be a positive integer")
    elif n == 0:
        return (0)
    elif n == 1:
        return (1)
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

n = int(input("Enter the nth Fibonacci number to find (starting from 0): "))
print (fibonacci(n))