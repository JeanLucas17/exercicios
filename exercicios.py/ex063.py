print("Sequencia de Fibonacci!")
n = int(input("Digite quantos termos quer ver: "))

t1 = 0
t2 = 1
count = 2

print(f"{t1} -> {t2}", end="")
while count < n:
    t3 = t1 + t2
    print(f" -> {t3}", end="")
    t1 = t2
    t2 = t3
    count += 1
