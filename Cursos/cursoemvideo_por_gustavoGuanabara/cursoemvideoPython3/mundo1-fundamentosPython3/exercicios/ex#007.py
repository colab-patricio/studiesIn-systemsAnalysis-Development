'''Desafio #007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.'''

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
print('A média entre as notas {} e {} vale {:.1f}'.format(nota1, nota2, ((nota1 + nota2) / 2)))