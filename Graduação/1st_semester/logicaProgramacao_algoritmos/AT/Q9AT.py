'''9. Faça um programa que receba um número e que calcule e mostre a tabuada desse número.'''

numero = int(input("Digite um número: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
