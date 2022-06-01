from random import randint
from random import choice

# ♠♣♥♦

class Baralho:
    def __init__(self):
        numero = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Dama', 'Rei'])
        naipe = choice(['Paus', 'Ouros', 'Copas', 'Espadas '])
        self.numero = numero
        self.naipe = naipe


    def gendeck(self):
        carta = self.numero, self.naipe
        deck = []
        while len(deck) != 3:
            try:
                if not carta in deck:
                    deck.append(carta)
            except:
                carta = self.numero, self.naipe
            carta = self.numero, self.naipe
        return deck

c1 = Baralho

print(c1)
print(c1.gendeck(c1))

#vitoria ou derrota, recebe >pontuação do jogador e da cpu
#retorna True = Vitoria, False = Derrota