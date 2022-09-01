import random

escolhe_dica = int(input("Escolha uma dica: (1) Fruta (2) Animal (3) Cor \n"))
while (escolhe_dica > 3) or (escolhe_dica < 1):
    print("Digite um número válido!")
    escolhe_dica = int(input("Escolha uma dica: (1) Fruta (2) Animal (3) Cor \n"))




if escolhe_dica == 1:
    arquivo = open("frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    print(palavra_secreta)

elif escolhe_dica == 2:
    arquivo = open("animal.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    print(palavra_secreta)

else:
    arquivo = open("cor.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    print(palavra_secreta)