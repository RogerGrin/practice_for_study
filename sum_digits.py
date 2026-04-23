def sum_digits(n):
    if n == 0:
        return n
    else:
        return n % 10 + sum_digits(n // 10)        
  
n = int(input())

print(sum_digits(n))

summa = 0
new_n = n
while new_n != 0:
    step = new_n % 10
    summa += step
    new_n //= 10

print(summa)