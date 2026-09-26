'''Exercício #004 - Python3 mundo 1: fundamentos - Curso em Video por Gustavo Guanabara
crie um programa que leia algo informado pelo teclado e mostre na tela seu tipo primitivo e
todas as informações possíveis sobre ele.'''

insertInformacao = input('Insira um dado qualquer: ')
print(insertInformacao)

print(type(insertInformacao))
print('O dado inserido é numérico? ', insertInformacao.isnumeric())
print('O dado inserido é alfabético? ', insertInformacao.isalpha())
print('O dado inserido é alfanumérico? ', insertInformacao.isalnum())
print('O dado inserido é um identificador válido? ', insertInformacao.isidentifier())
print('É possível imprimir o dado inserido? ', insertInformacao.isprintable())
print('O dado digitado está apenas em maísculas?', insertInformacao.isupper())