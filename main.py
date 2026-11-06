from src.models.card import Card
from src.models.card_version import CardVersion

print("One Piece TCG Scanner")

# Reformulei o código para evitar repetição, aloquei abaixo a lista e as variáveis em sequencia:
cartas = []
card1 = Card("Hibari", "EB03-008", "Extra Booster: One Piece Heroines Edition (EB03)", "Character", "Rara")
card2 = Card("King", "OP17-064", "The World's Strongest Warriors (OP-17)", "Character", "Normal")
card3 = Card("There You Are, Sore Loser", "EB03-020", "Extra Booster: One Piece Heroines Edition (EB03)", "Event Card", "Normal")
 
# Aqui irei tentar criar uma função para adicionar carta:
print('---------------------------------------------------------------------------------------------------------------')
def adicionar_carta(colecao, nova_carta):
    colecao.append(nova_carta)


adicionar_carta(cartas, card1)
adicionar_carta(cartas, card2)
adicionar_carta(cartas, card3)
print('---------------------------------------------------------------------------------------------------------------')

# criar uma função para simplificar o uso do for, e atualizar o código para ficar mais simples e fácil de entender:

def listar_cartas(lista):
    for item in lista:
        print(f'Nome: {item.name}\nCódigo: {item.card_code}\nRaridade: {item.rarity}\nColeção: {item.collection}')
        print('-------------------------------------------------------------------------------------------------------')
listar_cartas(cartas)






