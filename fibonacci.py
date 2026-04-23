# рекурсивно
def fibonacci(n):
    if (n > 2):
        return fibonacci(n - 2) + fibonacci(n - 1)
    elif (n == 2):
        return 1
    else:
        return 0
    
print(fibonacci(6))
