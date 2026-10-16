'''23. Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião em
relação ao filme: ótimo – 3, bom – 2, regular – 1. Faça um programa que receba a idade e a opinião de 15
espectadores e que calcule e mostre:
a) a média das idades das pessoas que responderam ótimo;
b) a quantidade de pessoas que responderam regular;
c) a percentagem de pessoas que responderam bom entre todos os espectadores analisados.'''

soma_idades_otimo = 0
qtd_otimo = 0
qtd_regular = 0
qtd_bom = 0

espectador = 1

while espectador <= 15:
    print(f"\nEspectador {espectador}")

    idade = int(input("Digite a idade: "))
    opiniao = int(input("Opinião (3-Ótimo, 2-Bom, 1-Regular): "))

    if opiniao == 3:
        soma_idades_otimo += idade
        qtd_otimo += 1
    elif opiniao == 2:
        qtd_bom += 1
    elif opiniao == 1:
        qtd_regular += 1

    espectador += 1

media_idades = (
    soma_idades_otimo / qtd_otimo
    if qtd_otimo > 0 else 0
)

porcentagem_bom = qtd_bom * 100 / 15

print("a) Média das idades (ótimo):", f"{media_idades:.2f}")
print("b) Quantidade de respostas regular:", qtd_regular)
print("c) Porcentagem de respostas bom:", f"{porcentagem_bom:.2f}%")
