def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        print("Recursing with input: {0}".format(n))
        return n * factorial(n - 1)

print(factorial(999))