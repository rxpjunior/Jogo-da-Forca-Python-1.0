# Jogo da Forca em Python
# Roberto Pereira - 2021

import random
# Lendo o arquivo de texto com as palavras separadas por virgula e salvando em uma lista
dicionario = open("dicionario.txt", 'r')
for linha in dicionario:
    listaPalavras = linha.split(",")
limite = len(listaPalavras)

n = random.randint(0, (limite - 1))

palavraSecreta = listaPalavras[n]
palavraSecreta = palavraSecreta.upper()
palavraGerada = ""
contErros = 0
letrasCertas = []

def imprimeBoneco(x):
    if x == 0:
        print("Erros: ", x)
    elif x == 1:
        print(" o ")
        print("Erros: ",x)
    elif x == 2:
        print(" o ")
        print(" | ")
        print("Erros: ", x)
    elif x == 3:
        print(" o ")
        print(' |\\')
        print("Erros: ", x)
    elif x == 4:
        print(" o ")
        print('/|\\')
        print("Erros: ", x)
    elif x == 5:
        print(" o ")
        print('/|\\')
        print("/  ")
        print("Erros: ", x)
    elif x == 6:
        print(" o ")
        print('/|\\')
        print("/ \\")
        print("Erros: ", x)
    elif x == 7:
        print(" o ")
        print("---")
        print('/|\\')
        print("/ \\")
        print("Erros: ", x)

print("JOGO DA FORCA")
print("Suas tentativas: " + len(palavraSecreta)*'_')

while contErros < 7:
    aux = input("Entre com uma letra: ")
    if len(aux) > 1:
        print("Você entrou com mais de uma letra. Isso não é permitido!\n")
        continue
    if aux.upper() in letrasCertas:
        print("Vc já havia adicionado a letra")
    elif aux.upper() in palavraSecreta:
        letrasCertas.append(aux.upper())
        print("Parabéns, uma letra você acertou!")
    else:
        print("Não existe esta letra na palavra")
        contErros += 1
    for x in palavraSecreta:
        if x in letrasCertas:
            palavraGerada = palavraGerada + x
        else:
            palavraGerada = palavraGerada + '_'
        if palavraSecreta == palavraGerada:
            print("Você acertou!!!!. A palavra correta é: " + palavraSecreta)
            break
    print("Suas tentativas: " + palavraGerada)
    imprimeBoneco(contErros)
    print("\n")
    if palavraSecreta == palavraGerada:
        print("VOCÊ VENCEU!!!")
        break
    if contErros != 7:
        palavraGerada = ""
if palavraSecreta != palavraGerada:
    print("VOCÊ PERDEU!!!")
    print("Mais sorte da próxima vez")
    imprimeBoneco(contErros)
print("A palavra secreta era: ", palavraSecreta, "e você conseguiu chegar até: ", palavraGerada)

