a1 = int(input("1ª Termo da PA: "))
r = int(input("Razão da PA: "))

termos = 10
count = 0

while termos > 0:
    count = 0
    while count < termos:
        print(a1)
        a1 += r
        count += 1
    termos = int(input("Se quer continuar digite mais termos, se quer parar digite 0: "))
