print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("Digite o seu numero: "))

if (numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    
    if (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")
