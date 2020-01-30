import random


def jogar():

    imprime_mensagem_de_abertura()
    palavra_secreta = carrega_palavra_secreta()

    # pra cada posicao da palavra secreta coloca um "_"
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_de_vitoria()
    else:
        imprime_mensagem_de_derrota()

def imprime_mensagem_de_derrota():
    print("Você perdeu")

def imprime_mensagem_de_vitoria():
    print("Você ganhou")


# funcao que verifica se a letra inserida pelo usuario
# existe na palavra secreta, se existir a letra colocada na posicao
# em que se encontra na palavra secreta
def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1


def pede_chute():
    chute = input("Qual é a letra? ")
    # a funcao strip() serve para tirar os espaços em branco da string e o upper() pra deixa-la em maiusculo
    chute = chute.strip().upper()
    return chute


def inicializa_letras_acertadas(palavra):
    # pra cada posicao da palavra secreta coloca um "_"
    letras_acertadas = ["_" for letra in palavra]
    return letras_acertadas


def carrega_palavra_secreta():
    arquivo = open("jogos/lista_palavras.txt", "r")

    palavras = []  # cria lista
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def imprime_mensagem_de_abertura():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")


if (__name__ == "__main__"):
    jogar()
