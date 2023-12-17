'''
Nick Boni
7/19/2018

This file lays out all the enemy beasts and ghouls 
the player will encounter in the game.
'''

# imports Creature, randint, choice, choices
from creature import *

# imports Item, all common items
from common_items import *

#################################################################

class Rat(Creature):

	def __init__(self):
		'''Rats are a basic enemy at the beginning of the game.
		Pretty much used to grind through your first few levels,
		and then a nuisance for the rest of the game.'''

		Creature.__init__(self)

		self.LEVEL = randint(1,3)

		self.EXP = randint(0, self.determine_exp()-1)
		self.MAXHP = randint(1,7)
		self.HP = self.MAXHP
		self.ATK = randint(1,5)
		self.DEF = randint(1,5)
		self.SPD = randint(5,10)
		self.LCK = randint(10,30)
		self.SNK = randint(20,50)
		self.CHM = 0
		self.INT = randint(15,45)
		self.name = 'Rat'

		self.check_attrs()

		if randint(0,101) > 75:
			self.inventory.append(Stone())

#################################################################

class Goblin(Creature):
	'''Goblins are levels 5-10, a harder beginning enemy.
	Their ATK and DEF stats are around their own level.
	They are unlucky. They can be fast. They have no CHM or INT.'''

	def __init__(self):

		Creature.__init__(self)

		self.LEVEL = randint(5,10)

		self.EXP = randint( 0, self.determine_exp()-1 )
		self.MAXHP = 10 + ( (self.LEVEL-5) * randint(0,3) )
		self.HP = self.MAXHP
		self.ATK = self.LEVEL + randint(0,5)
		self.DEF = self.LEVEL + randint(-5,0)
		self.SPD = self.LEVEL + randint(0,5)
		self.LCK = self.LEVEL + randint(-(self.LEVEL-1),0)
		self.SNK = self.LEVEL + randint(-2,8)
		self.CHM = 0
		self.INT = 0
		self.name = 'Goblin'

		self.check_attrs()

		if randint(0,101) > 75:
			self.inventory.append(Skull())

#################################################################

class Bear(Creature):
	'''Bears are levels 10-20, a fearsome early-game enemy.
	They have high ATK. They are slow. They are intelligent.'''

	def __init__(self):

		Creature.__init__(self)

		self.LEVEL = randint(10,20)
			
		self.EXP = randint( 0, self.determine_exp()-1 )
		self.MAXHP = self.LEVEL + randint(10,15)
		self.HP = self.MAXHP
		self.EXP = randint(0,self.determine_exp()-1)
		self.ATK = self.LEVEL + randint(10,20)
		self.DEF = self.LEVEL + randint(-5,5)
		self.SPD = self.LEVEL + randint(-10,-5)
		self.LCK = self.LEVEL + randint(-5,5)
		self.SNK = self.LEVEL + randint(-15,-5)
		self.CHM = 0
		self.INT = self.LEVEL + randint(0,7)
		self.name = 'Bear'

		self.check_attrs()

		'''
		if randint(0,101) > 75:
			self.inventory.append(Berry())
		'''

#################################################################

class Warlock(Creature):
	'''Warlocks are levels 25-40, a midgame dungeon boss. 
	Their ATK is based on their INT. They have very low DEF.
	They are very intelligent.'''

	def __init__(self):

		Creature.__init__(self)

		self.LEVEL = randint(25,40)
		
		self.EXP = randint( 0, self.determine_exp()-1 )
		self.MAXHP = self.LEVEL + randint(0,15)
		self.HP = self.MAXHP
		self.EXP = randint(0,self.determine_exp()-1)
		# ATK stat is set below
		self.DEF = self.LEVEL + randint(-20,-5)
		self.SPD = self.LEVEL - randint(3,7)
		self.LCK = self.LEVEL + randint(0,5)
		self.SNK = self.LEVEL - randint(5,self.LEVEL)
		self.CHM = 0
		self.INT = self.LEVEL + randint(20,25)
		self.name = 'Warlock'

		# A Warlock's spellcasting ability is determined
		# by his intelligence.
		self.ATK = self.INT + randint(-10,10)

		self.check_attrs()

#################################################################

from mechanics import battle, load_file

if __name__ == '__main__':

	hero = load_file()
	g = Goblin()
	b = Bear()

	print('Goblin:\n' + g.gen_stats_string())
	print('Bear:\n' + b.gen_stats_string())

	battle(hero,g,b)