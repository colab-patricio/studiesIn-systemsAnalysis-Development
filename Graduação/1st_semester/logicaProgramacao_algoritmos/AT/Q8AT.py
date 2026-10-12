
faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0

for i in range(1, 16):
    idade = int(input(f"Digite a idade da pessoa {i}: "))

    if idade <= 15:
        faixa1 += 1
    elif idade <= 30:
        faixa2 += 1
    elif idade <= 45:
        faixa3 += 1
    elif idade <= 60:
        faixa4 += 1
    else:
        faixa5 += 1

print("\nQuantidade por faixa etária:")
print("1ª faixa (até 15 anos):", faixa1)
print("2ª faixa (16 a 30 anos):", faixa2)
print("3ª faixa (31 a 45 anos):", faixa3)
print("4ª faixa (46 a 60 anos):", faixa4)
print("5ª faixa (61 anos ou mais):", faixa5)

percentual1 = faixa1 / 15 * 100
percentual5 = faixa5 / 15 * 100

print(f"Percentual da 1ª faixa: {percentual1:.2f}%")
print(f"Percentual da 5ª faixa: {percentual5:.2f}%")
