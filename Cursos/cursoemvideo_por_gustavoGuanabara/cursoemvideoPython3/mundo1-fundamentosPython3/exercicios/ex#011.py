'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
área e quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta
uma área de 2m²'''

import math # Importar biblioteca

l_parede = float(input('Qual a largura da parede em metros? '))
h_parede = float(input('Qual a altura da parede em metros? '))

area = l_parede * h_parede
qtd_tinta_necessária = area / 2

# math.ceil() significa arredondar para cima
qtd_tinta_necessária = math.ceil(qtd_tinta_necessária)

print('Para uma parede de {:.3f}m² será necessário {:.1f}L de tinta'.format(area, qtd_tinta_necessária))