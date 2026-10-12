'''12. Faça um programa que receba a idade, a altura e o peso de 25 pessoas. Calcule e mostre:
a) a quantidade de pessoas com idade superior a 50 anos;
b) a média das alturas das pessoas com idade entre 10 e 20 anos;
c) a percentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.'''

maiores_50 = 0
soma_alturas = 0.0
quantidade_10_20 = 0
menores_40kg = 0

for i in range(1, 26):
    print(f"\nPessoa {i}")

    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura em metros: "))
    peso = float(input("Digite o peso em kg: "))

    if idade > 50:
        maiores_50 += 1

    if 10 <= idade <= 20:
        soma_alturas += altura
        quantidade_10_20 += 1

    if peso < 40:
        menores_40kg += 1

if quantidade_10_20 > 0:
    media_alturas = soma_alturas / quantidade_10_20
else:
    media_alturas = 0

percentual = menores_40kg / 25 * 100

print("\n--- RESULTADOS ---")
print("Pessoas com mais de 50 anos:", maiores_50)
print(f"Média das alturas entre 10 e 20 anos: {media_alturas:.2f} m")
print(f"Percentual com peso inferior a 40 kg: {percentual:.2f}%")
