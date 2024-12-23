'''
Nick Boni
10/18/2020

This class defines the Item.
'''

class Item:
	'''Base class for all items in the game.'''

	def __init__(
		self,
		name='',
		value = 0,
		quest_item = False,
		active = False,
		description = ''
		):

		self.name = name
		self.value = value
		self.quest_item = quest_item
		self.active = active
		self.description = description

	def inspect(self):
		outstr = 'Name: %s\n\
		Value: %d\n\
		Description: %s'%(
			self.name,
			self.value,
			self.description
			)
		return outstr


#################################################################

if __name__ == '__main__':

	from creatures.people.hero import Hero
	from mechanics import load_file

	hero = load_file()

	h = Item('hotdog')
	r = Item('rock')

	choice = input('Which item wilt thou take? Type 1 for hotdog, 2 for rock: ')
	if choice == '1':
		hero.inventory.append(h)
	elif choice == '2':
		hero.inventory.append(r)
	else:
		print('You fool!')

	print(hero.inventory)

	for item in hero.inventory:
		print(item.name)	