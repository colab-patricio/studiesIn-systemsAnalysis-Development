""""Faça um programa que receba uma hora (uma variável para hora e outra para minutos), calcule e mostre:
a. A hora convertida em minutos;
b. O total dos minutos, ou seja, os minutos digitados mais a conversão anterior;
c. O total dos minutos convertidos em segundos."""

# Declarando as variáveis
hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))

hora_em_minutos = hora * 60 # a) Hora convertida em minutos

total_minutos = hora_em_minutos + minutos # b) Total de minutos

# c) Total de minutos convertido em segundos
total_segundos = total_minutos * 60

# Resultados
print("Hora convertida em minutos:", hora_em_minutos)
print("Total de minutos:", total_minutos)
print("Total de minutos em segundos:", total_segundos)