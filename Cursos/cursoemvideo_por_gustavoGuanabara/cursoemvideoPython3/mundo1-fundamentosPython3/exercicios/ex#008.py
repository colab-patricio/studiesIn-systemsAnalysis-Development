'''Desafio #008: Escreva um programa que leia um valor em metros e o exia convertido em centímetros e milímetros'''

valor_em_metros = float(input('Informe o valor em metros: '))
valor_cent = valor_em_metros * (10 ** 2)
valor_mm = valor_em_metros * (10 ** 3)

print('{} metros equivale a {:.2f}cm ou a {:.2f}mm'.format(valor_em_metros, valor_cent, valor_mm))

# Desafio extra: metros para Km
print('{}m equivale a {}Km'.format(valor_em_metros, (valor_em_metros / 1000)))