from items.quest_items import Coin_for_Alms, Wernicke_Candelabra
from creatures.people.hero import Hero

h = Hero()
coin = Coin_for_Alms()
cand = Wernicke_Candelabra()

print(coin.name)
print(cand.name)


response = input("Will you take the coin? ")
if response == 'y':
    h.inventory.append(coin)
    print(h.gen_inventory_string())