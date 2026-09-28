'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
o carro custa R$60,00/dia e R$0,15/Km rodado.'''

Km = float(input('Qual a quantidade de Km percorrido? '))
dias = int(input('Por quantos dias foi alugado? '))
valor_aluguel = (60 * dias) + (Km * 0.15)

print('O total a pagar pelo aluguel do carro é de R$', valor_aluguel)