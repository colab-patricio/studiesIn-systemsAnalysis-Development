'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário c/ 15% de aumento'''

salario_atual = float(input('Digite seu salário atual: R$'))
salario_reajustado = salario_atual * 1.15

print('O salário reajustado em 15% de aumento é R${:.2f}'.format(salario_reajustado))