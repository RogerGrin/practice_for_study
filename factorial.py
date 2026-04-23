# рекурсивно
def factorial(n):
    if (n > 1):
        return n * factorial(n - 1)
    else:
        return 1

# итеративно 
n = int(input())
while n < 0:
    print(f'повторите попытку\n')
    n = int(input())

print(factorial(n))

product = 1

while n > 1:
    product *= n
    n -= 1

print(product)
