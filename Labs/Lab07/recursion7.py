fibonacci_runtime = ""

def fibonacci(n):
    global fibonacci_runtime
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibonacci_runtime += "fibonacci({}) ".format(n)
        return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(5))
print("Runtime:", fibonacci_runtime)
fibonacci_runtime = "O(2^n)"

