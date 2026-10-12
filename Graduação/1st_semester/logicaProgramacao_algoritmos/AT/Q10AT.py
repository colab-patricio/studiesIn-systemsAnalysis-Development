'''10. Faça um programa que mostre as tabuadas dos números de 1 a 10.
'''

for numero in range(1, 11):
    print(f"\nTabuada do {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
