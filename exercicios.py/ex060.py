from math import factorial

num = int(input("Digite um numero: "))
fatorial = factorial(num)
n = num
count = 0

print(f"Fatorial de {num} \n {num}! = ", end="")
while count < num:
    if count == 0:
        print(n, end="")
    else:
        print(f" x {n}", end="")
    n -= 1
    count += 1

print(f" = {fatorial}")
