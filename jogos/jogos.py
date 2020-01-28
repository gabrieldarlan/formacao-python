import forca
import adivinhacao

print("***************************")
print("      Escolha seu jogo     ")
print("***************************")


def escolher_jogo():
    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual é o jogo? "))

    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        adivinhacao.jogar()


if (__name__ == "__main__"):
    escolher_jogo()
