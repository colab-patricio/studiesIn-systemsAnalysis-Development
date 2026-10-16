'''27. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma cidade, em um determinado dia.
Para cada casa consultada foi fornecido o número do canal (4, 5, 7, 12) e o número de pessoas que estavam
assistindo àquele canal. Se a televisão estivesse desligada, nada era anotado, ou seja, essa casa não entrava na
pesquisa. Faça um programa que:
a) Leia um número indeterminado de dados (número do canal e o número de pessoas que estavam assistindo);
b) Calcule e mostre a percentagem de audiência de cada canal;
Para encerrar a entrada de dados, digite o número do canal ZERO.'''

canal4 = 0
canal5 = 0
canal7 = 0
canal12 = 0

while True:
    canal = int(input("Digite o canal (0 para encerrar): "))

    if canal == 0:
        break

    pessoas = int(input("Número de pessoas assistindo: "))

    if canal == 4:
        canal4 += pessoas
    elif canal == 5:
        canal5 += pessoas
    elif canal == 7:
        canal7 += pessoas
    elif canal == 12:
        canal12 += pessoas
    else:
        print("Canal inválido!")

total = canal4 + canal5 + canal7 + canal12

if total > 0:
    print("Audiência do canal 4:", round(canal4 / total * 100, 2), "%")
    print("Audiência do canal 5:", round(canal5 / total * 100, 2), "%")
    print("Audiência do canal 7:", round(canal7 / total * 100, 2), "%")
    print("Audiência do canal 12:", round(canal12 / total * 100, 2), "%")
else:
    print("Nenhuma pessoa foi contabilizada.")
