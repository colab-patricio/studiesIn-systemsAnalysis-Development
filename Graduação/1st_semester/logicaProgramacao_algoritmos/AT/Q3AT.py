'''3. Faça um programa que calcule e mostre o produto dos números primos entre 92 e 1.478'''

produto = 1

for num in range(93, 1479):
    primo = True

    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        produto *= num

print("Produto dos números primos entre 92 e 1.478 é igual a: \n", produto)
