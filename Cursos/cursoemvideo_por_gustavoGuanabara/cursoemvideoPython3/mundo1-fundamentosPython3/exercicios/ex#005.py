'''Desafio #005: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor'''

valor_digitado = int(input('Digite um valor inteiro qualquer: '))
print('O sucessor e o antecessor de {} são, respectivamente {} e {}.'.format(valor_digitado, (valor_digitado + 1), (valor_digitado - 1)))