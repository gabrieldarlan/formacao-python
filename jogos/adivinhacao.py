print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("Digite o seu numero: "))

if (numero_secreto==chute):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do jogo")
