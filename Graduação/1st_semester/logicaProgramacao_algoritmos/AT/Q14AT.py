'''14. Faça um programa que receba a idade, o peso, a altura, a cor dos olhos (A – Azul, P – Preto, V – Verde e C –
Castanho) e a cor dos cabelos (P – Preto, C – Castanho, L – Louro e R – Ruivo) de 20 pessoas, calcule e mostre:
a) a quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos;
b) a média das idades das pessoas com altura inferior a 1,50;
c) a porcentagem de pessoas com olhos azuis entre todas as pessoas analisadas;
d) a quantidade de pessoas ruivas e que não possuem olhos azuis.
'''

TOTAL_PESSOAS = 20

qtd_idade_peso = 0
soma_idades_altura = 0
qtd_altura_menor = 0
qtd_olhos_azuis = 0
qtd_ruivas_sem_olhos_azuis = 0

print(f"Cadastro de {TOTAL_PESSOAS} pessoas")

for i in range(1, TOTAL_PESSOAS + 1):
    print(f"\nPessoa {i}:")
    idade = int(input("Idade: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    cor_olhos = input("Cor dos olhos (A - Azul, P - Preto, V - Verde, C - Castanho): ").strip().upper()
    cor_cabelos = input("Cor dos cabelos (P - Preto, C - Castanho, L - Louro, R - Ruivo): ").strip().upper()

    # a) Idade > 50 e peso < 60
    if idade > 50 and peso < 60:
        qtd_idade_peso += 1

    # b) Altura < 1.50
    if altura < 1.50:
        soma_idades_altura += idade
        qtd_altura_menor += 1

    # c) Olhos azuis ('A')
    if cor_olhos == 'A':
        qtd_olhos_azuis += 1

    # d) Ruivas ('R') e que NÃO possuem olhos azuis ('A')
    if cor_cabelos == 'R' and cor_olhos != 'A':
        qtd_ruivas_sem_olhos_azuis += 1

# Processamento do item b
if qtd_altura_menor > 0:
    media_idade_altura = soma_idades_altura / qtd_altura_menor
else:
    media_idade_altura = 0.0

# Processamento do item c
porcentagem_olhos_azuis = (qtd_olhos_azuis / TOTAL_PESSOAS) * 100

print("\nRESULTADOS")
print(f"a) Pessoas com idade > 50 e peso < 60kg: {qtd_idade_peso}")
if qtd_altura_menor > 0:
    print(f"b) Média de idade das pessoas com altura < 1.50m: {media_idade_altura:.2f} anos")
else:
    print("b) Nenhuma pessoa cadastrada possui altura inferior a 1.50m.")
print(f"c) Porcentagem de pessoas com olhos azuis: {porcentagem_olhos_azuis:.2f}%")
print(f"d) Pessoas ruivas que não possuem olhos azuis: {qtd_ruivas_sem_olhos_azuis}")