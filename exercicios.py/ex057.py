sexo = str(input("Digite o sexo [M/F]: ")).upper().strip()

while sexo not in ["M", "F"]:
    print("Sexo invalido!")
    sexo = str(input("Apenas [M/F]: ")).upper().strip()

if sexo in "M":
    print(f"Você é Homem!")
else:
    print("Você é Mulher!")
 