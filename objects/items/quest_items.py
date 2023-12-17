'''
Nicholas Boni
08/26/2022

This file lays out the quest items of the game.
'''

from item import Item

#################################################################

class Wernicke_Candelabra(Item):
	def __init__(self):

		Item.__init__(self,
			name="Wernicke's Candelabra",
			value=75,
			quest_item=True,
			description="A delicately-gilt golden candelabra, with shapes of creeping ivy twining the tines. The candleholes are bizarrely narrow - you've never seen a candle narrow enough to fit in these slots."
			)

#################################################################

if __name__ == '__main__':
	from hero import Hero
	from mechanics import load_file

	h = Hero()

	choice = input('Wilt thou take the Candelabra? (y/n) ')

	if choice.upper() == 'Y':
		h.inventory.append(Wernicke_Candelabra())
	else:
		print('You fool!')

	print(h.gen_inventory_string())

	choice = input('Inspect inventory? (y/n) ')

	if choice.upper() == 'Y':
		for item in h.inventory:
			outstr = 'Name: %s\nDescription: %s'%(item.name,item.description)
			print(outstr)
	else:
		print('You fool!')