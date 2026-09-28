'''Desafio #006 Crie um algoritmo que leia um número e mostre o dobro, o triplo e a raiz quadrada deste'''

num = float(input('Digite um número qualquer: '))
dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** (1/2)

print('Num. digitado: ', num)
print('O dobro vale {:.2f}. \n O triplo vale {:.2f}. \n A raiz quadrada vale {:.2f}.'.format(dobro, triplo, raiz_quadrada))
