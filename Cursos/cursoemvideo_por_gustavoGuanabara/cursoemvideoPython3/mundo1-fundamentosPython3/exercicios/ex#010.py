'''Exercício #010: Crie um programa que leia quanto de dinheiro uma pessoa tem
na carteira e quantos doláres ela pode comprar. Considere US$1,00 = R$5,22'''

quantia_em_reais = float(input('Quanto de dinheiro você tem na carteira? R$'))
quantia_em_dolar = quantia_em_reais / 5.22

print('Com tantos R${} você pode comprar US${:.2f}.'.format(quantia_em_reais, quantia_em_dolar))