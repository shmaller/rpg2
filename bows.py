'''
Nick Boni
10/19/2020

This file defines the Bow class of Weapons in the game.
'''

from weapon import Weapon
from arrows import *
from careers import Archer

class Bow(Weapon):
	def __init__(self):
		Weapon.__init__(self)
		self.user_class = Archer

	def get_atk_value(self,user):
		if user.has(self.ammo):
			return self.atk_boost
		else:
			print('\n%s is out of %ss!\n'%(user.name,self.ammo.name))
			return 0

#################################################################

class Slingshot(Bow):
	def __init__(self):

		Bow.__init__(self)

		self.name = 'Slingshot'
		self.ammo = Stone()
		self.value = 10
		self.quest_item = False
		self.atk_boost = 2
		self.condition = 25
		self.description = 'A forked, flexible treebranch whittled down to handheld size, with a springy band to fling small stones. Little more than a children\'s toy.'

#################################################################

class Longbow(Bow):
	def __init__(self):

		Bow.__init__(self)

		self.name = 'Longbow'
		self.ammo = Arrow()
		self.value = 45
		self.quest_item = False
		self.atk_boost = 25
		self.condition = 50
		self.description = 'A long, curved wooden bow, hewn from a single piece of wood. \'Tis nearly as tall as thee. Takes great strength to draw back, and fires an arrow smartly.'

#################################################################

class Crossbow(Bow):
	def __init__(self):

		Bow.__init__(self)

		self.name = 'Crossbow'
		self.ammo = Bolt()
		self.value = 150
		self.quest_item = False
		self.atk_boost = 40
		self.condition = 80
		self.description = 'A large, heavy, shoulder-mounted wooden contraption. Upon a broad beam of timber is mounted a rigid metal bow. The firm cord must be drawn back prior to firing. The racket and recoil of a loosed bolt turns thy stomach in bitter sympathy for thy enemy.'

#################################################################

if __name__ == "__main__":

	from fileops import load_file
	# from arrows import Stone
	from bestiary import Goblin

	hero = load_file()

	g = Goblin()

	a = Archer(hero)

	s = Slingshot()

	input(s.inspect())

	a.inventory.append(s)
	print(a.gen_inventory_string())

	# s.has_ammo(a)
	print(s.get_atk_value(a))

	a.inventory.append(Stone())

	print('does archer have ammo?')
	print(a.has(s.ammo))

	print(a.gen_inventory_string())

	print(s.get_atk_value(a))

	a.inventory = []

	a.inventory.append(Crossbow())
	a.inventory.append(Bolt())

	print(a.gen_inventory_string())

	for item in a.inventory:
		print(item.inspect())

	a.inventory = []

	a.inventory.append(Longbow())
	a.inventory.append(Arrow())

	print(a.gen_inventory_string())

	for item in a.inventory:
		print(item.inspect())

	a.inventory = []

	l = Longbow()

	a.inventory.append(l)
	a.inventory.append(Bolt())

	print('does archer have ammo?')
	print(a.has(l.ammo))

	# s.has_ammo(a)