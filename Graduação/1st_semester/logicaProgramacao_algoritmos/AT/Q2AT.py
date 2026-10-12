'''2. Faça um programa que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma:
S = 1 + ½ + ⅓ + ¼ + … + 1/n'''


n = int(input("Digite um número inteiro positivo: "))

soma = 0.0

for i in range(1, n + 1):
    soma += 1 / i

print("Resultado da soma:", soma)
