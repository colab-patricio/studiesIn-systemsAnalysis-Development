'''24. Uma firma fez uma pesquisa de mercado para saber se as pessoas gostaram ou não de um novo produto
lançado no mercado. Para isso, forneceu o sexo do entrevistado e sua resposta (S – Sim ou N – Não). Sabe-se que
foram entrevistadas dez pessoas. Faça um programa que calcule e mostre:
a) o número de pessoas que respondeu sim;
b) o número de pessoas que respondeu não;
c) o número de mulheres que respondeu sim;
d) a percentagem de homens que respondeu não entre todos os homens analisados.'''

sexos = []
respostas = []

for i in range(10):
    sexo = input("Digite o sexo (M/F): ").upper()
    resposta = input("Gostou do produto? (S/N): ").upper()

    sexos.append(sexo)
    respostas.append(resposta)

sim = respostas.count("S")
nao = respostas.count("N")

mulheres_sim = 0
homens = 0
homens_nao = 0

for i in range(10):
    if sexos[i] == "F" and respostas[i] == "S":
        mulheres_sim += 1

    if sexos[i] == "M":
        homens += 1
        if respostas[i] == "N":
            homens_nao += 1

print("Respondeu sim:", sim)
print("Respondeu não:", nao)
print("Mulheres que responderam sim:", mulheres_sim)

if homens > 0:
    percentual = homens_nao / homens * 100
    print("Percentual de homens que responderam não:",
          percentual, "%")
else:
    print("Não foram entrevistados homens.")