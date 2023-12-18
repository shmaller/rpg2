'''
Nick Boni
10/23/2020

This file defines all Daggers in the game.
'''

from weapon import Weapon

class Dagger(Weapon):
	def __init__(self):
		Weapon.__init__(self)
		# self.user_class = Knave

class SteakKnife(Dagger):
	def __init__(self):
		Dagger.__init__(self)
		self.name = 'Steak Knife'
		self.atk_boost = 2
		self.value = 0
		self.condition = 20
		self.description = 'A rusty table knife.'

class Shiv(Dagger):
	def __init__(self):
		Dagger.__init__(self)
		self.name = 'Shiv'
		self.atk_boost = 3
		self.value = 0
		self.condition = 10
		self.description = 'A broken piece of a bone fork.'

class BoneDagger(Dagger):
	def __init__(self):
		Dagger.__init__(self)
		self.name = 'Bone Dagger'
		self.atk_boost = 6
		self.value = 5
		self.condition = 50
		self.description = 'A short blade whittled from a mammoth\'s rib.'

class Sai(Dagger):
	def __init__(self):
		self.name = 'Sai'
		self.atk_boost = 8
		self.value = 25
		self.condition = 75
		self.description = 'A dagger with a long blade and a large, curved hilt.'

class Corvo(Dagger):
	def __init__(self):
		self.name = 'Corvo'
		self.atk_boost = 10
		self.value = 25
		self.condition = 60
		self.description = 'This short, curved knife looks as much like a farm implement as a weapon.'

class Dirk(Dagger):
	def __init__(self):
		Dagger.__init__(self)
		self.name = 'Dirk'
		self.atk_boost = 12
		self.value = 45
		self.condition = 60
		self.description = 'A simple blade in a leather scabbard. Corrosion and plainness suggest that this dagger may have spent its life among an austere people near the sea.'

class Stiletto(Dagger):
	def __init__(self):
		self.name = 'Stiletto'
		self.atk_boost = 18
		self.value = 50
		self.condition = 80
		self.description = 'A finely wrought dagger with a long, skinny blade which tapers to a vicious point.'

class Pugio(Dagger):
	def __init__(self):
		self.name = 'Pugio'
		self.atk_boost = 25
		self.value = 100
		self.condition = 85
		self.description = 'A well-kept relic of an ancient empire. The blade is of steel, and its sheath twinkles mysterious runes in silver and bronze.'

class Jutte(Dagger):
	def __init__(self):
		self.name = 'Jutte'
		self.atk_boost = 0
		self.value = 0
		self.condition = 100
		self.quest_item = True
		self.description = 'An ornate bronze baton in the shape of a dagger, carved with runes and visages of mythic monsters, with a sharp hook protruding from one side. Attached to the pommel is a silk tassel dyed rich hues of purple and gold. An imposing imperial seal is imprinted in the hilt.'

#################################################################

if __name__ == '__main__':
	from hero import Hero

	h = Hero()

	h.inventory.append(SteakKnife())

	print(h.gen_inventory_string())

	print(Jutte().description)

