'''Escreva um programa que converta uma temperatura em ºC para ºF
'''

celsius = float(input('Infome uma temperatura em ºC: '))
fahrenheit = (9 * celsius) / 5 + 32

print('{:.1f}ºC equivale a {:.1f}ºF'.format(celsius, fahrenheit))