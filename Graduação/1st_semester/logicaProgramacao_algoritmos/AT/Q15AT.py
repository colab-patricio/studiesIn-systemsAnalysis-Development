'''15. Faça um programa que receba dez números e que calcule e mostre a quantidade de números entre 30 e 90.
'''

contador = 0

for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número: "))

    if numero >= 30 and numero <= 90:
        contador += 1

print("Quantidade de números entre 30 e 90:", contador)
