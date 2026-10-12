'''7. Faça um programa que receba a idade de dez pessoas e que calcule e mostre a quantidade de pessoas com
idade maior ou igual a 18 anos.'''

contador = 0

for i in range(1, 11):
    idade = int(input(f"Digite a idade da pessoa {i}: "))

    if idade >= 18:
        contador += 1

print("Quantidade de pessoas com 18 anos ou mais:", contador)
