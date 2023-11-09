#THE JUMBLED GAME (Acerte as palavras)
import random

palavras = ["pai", "empresa", "ciência", "programação", "resistência", "ficção", "condição", "reverso", "computador", "python"]

palavra = random.choice(palavras)

game = random.sample(palavra, len(palavra))

game = " ".join(game)
print(f"A Palavra Confusa é: {game}")

player = input(f"Escreva o que você acha:")

if player.lower() == palavra:
    print(f"Correto! A {game} é {player}")
else:
    print(f"Incorreto! A {game} é {palavra}")    