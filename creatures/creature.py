'''
Nick Boni
7/17/2018

This file defines Creatures in the game. It is the
base class for all living things in the game.
'''

import random

#################################################################
#################################################################
#################################################################

class Creature:
	'''
	Base class for all living things in the game.
	Things Creatures can do:
	- Attack (another Creature)
	- Die
	- Speak (to another Creature)
	- Find
	- Woo (another Creature)
	'''

#################################################################

	def check_attrs(self):
		'''Accept Self as input. After Creature generation,
		verifies that all stats are above zero. If any are
		at or below zero, sets them to 5. No return value.'''

		attr_list = ['LEVEL','EXP','MAXHP','HP','ATK','DEF','SPD','LCK','SNK','CHM','INT']

		for attr in attr_list:
			if attr == 'EXP':
				continue
			if getattr(self,attr) <= 0:
				setattr(self,attr,5)

#################################################################

	def test_name(self,input_name,list_of_names_to_choose):
		'''Takes a Creature's name, and if it's an empty string,
		returns a choice from a list of alternate names.'''

		if input_name == '':
			return random.choice(list_of_names_to_choose)
		else:
			return input_name

#################################################################

	def __init__(
		self,
		LEVEL=1,
		EXP=0,
		MAXHP=15,
		HP=15,
		ATK=5,
		DEF=5,
		SPD=5,
		LCK=5,
		SNK=5,
		CHM=5,
		INT=5,
		name='',
		player=False,
		inventory=[],
		location=''
		):
		'''
		Assigns the following characteristics:
		- Level (int)
		- Experience points (int)
		- Max HP capacity (int)
		- Current HP (int)
		- Attack (int)
		- Defense (int)
		- Speed (int)
		- Luck (int)
		- Sneak (int)
		- Charm (int)
		- Name (str)
		- Whether this Creature is the player (bool)
		- An inventory (list of Item child objects)

		Returns None.
		'''

		self.LEVEL = LEVEL
		self.MAXHP = MAXHP
		self.HP = HP
		self.EXP = EXP
		self.ATK = ATK
		self.DEF = DEF
		self.SPD = SPD
		self.LCK = LCK
		self.SNK = SNK
		self.CHM = CHM
		self.INT = INT
		# self.name = self.test_name(name,['Creature'])
		self.name = name
		self.player = player
		self.inventory = inventory
		self.location = location

		self.check_attrs()

#################################################################

	def attack(self,other):
		'''
		Accepts the Creature object to be attacked as an input.

		Calculates the amount of damage done based on attacker
		and defender's stats, and deducts the damage done from
		the defender's HP stat.

		Returns None.
		'''
		from items.weapons.weapon import Weapon

		base_atk = int(self.ATK / 3)
		print('base atk factor %d'%base_atk)

		base_atk += self.determine_weapon_value()
		print('after weapon factor %d'%base_atk)

		# The chance of a critical hit is determined by random
		# chance, plus 1% of my Luck skill.
		crit_chance = ( random.randint(0,101) + (self.LCK / 100) )
		critical = False

		# A critical hit triples my base attack!
		if crit_chance >= 75:
			base_atk *= 3
			critical = True

		# The Attack Random Factor introduces chance into the attacking game.
		# A base attack does 33% of the attack stat. The A.R.F. adds an additional
		# additive or subtractive factor of 5% of the base attack stat.
		attack_rand_factor = random.randint( -int(self.ATK/20), int(self.ATK/20) )

		# Your defense is also taken into account. If my attack is higher than
		# your defense, I get a boost of half the difference between those stats.
		# If your defense is higher than my attack, my attack is cut by half
		# this difference.
		atk_def_diff = (self.ATK - other.DEF)
		defense_factor = int(atk_def_diff / 2)

		damage_done = base_atk + attack_rand_factor + defense_factor

		# An attack always does at least 1 damage.
		if damage_done <= 0:
			damage_done = 1

		# Set your HP to the proper value. HP can never go negative.
		if damage_done < other.HP:
			other.HP -= damage_done
		else:
			other.HP = 0

		# Display our results to the player.
		print('\n' + '*'*65 + '\n%s attacks %s!\n'%(self.name,other.name)) ################## resize box to window size

		if critical:
			print('A critical hit!\n')

		input('%s does %d damage. %s now has %d HP left.\n'%(
			self.name, damage_done, other.name, other.HP) + '*'*65 + '\n'
		)

#################################################################

	def die(self):
		'''
		Accepts no inputs.

		Checks character's HP stat. If zero, returns True and
		alerts the player that a character has died. If nonzero,
		returns False.
		'''

		if self.HP <= 0:
			print('%s died.\n'%self.name)
			return True
		else:
			return False

#################################################################

	def check_level_up(self):
		'''
		Accepts no inputs.

		A Creature levels up when it receives 10x its 
		current level in EXP.

		Checks if the object has 100 EXP. If so,
		the object calls level_up() and returns True. If not,
		returns False.
		'''

		if self.EXP >= (self.LEVEL * 10):
			self.level_up()
			return True
		else:
			return False

#################################################################

	def level_up(self):
		'''
		Accepts no inputs.

		Increments the character's level. If it's the user who
		levels up, prompts for three stats to boost. Then
		increments all stats, and removes 100 EXP to set the
		user back.

		If it's an NPC who levels up, selects three stats at
		random to boost, and levels up.

		Checks at the end of function to see if it's appropriate
		to level up again after subtracting 100 EXP.

		Returns None.
		'''
		attr_list = ['HP','ATK','DEF','SPD','LCK','SNK','CHM','INT']

		# Wait to actually update the attributes until the end of
		# the function, when were sure nothing's gone wrong.
		new_level = self.LEVEL + 1

		if self.player:

			print("You're now level %d!\n"%new_level)
			print("Choose three focus stats, pressing Enter after each one:\n\
			 HP, ATK, DEF, SPD, LCK, SNK, CHM, INT\n")
			
			traits = []
			
			for i in range(3):

				# prompt user for desired stat boost.
				trait = input().upper()

				# Check input for validity. If invalid input,
				# run the function again until we get one.
				if trait not in attr_list:
					print('That be not a valid attribute.\n')
					return self.level_up()

				if trait == "HP":
					trait = 'MAXHP'

				traits.append(trait)
		else:
			# NPCs just choose 3 stats at random to boost.
			print('\n%s is now level %d.\n'%(self.name,new_level))
			traits = random.choices(attr_list,k=3)

		for trait in traits:
			# Boost the focus areas by an extra +2 points.
			current_stat_val = getattr(self,trait)
			setattr(self, trait, current_stat_val+2)

		# Increase all stats.
		self.MAXHP += 3
		self.HP += 3   #self.MAXHP # Char is healed by level-up
		self.ATK += 1
		self.DEF += 1
		self.SPD += 1
		self.LCK += 1
		self.SNK += 1
		self.CHM += 1
		self.INT += 1

		# reset the EXP level.
		# if self.EXP < self.LEVEL*10:
		# 	self.EXP = 0
		# else:
		self.EXP -= self.LEVEL*10

		self.LEVEL += 1

		# Print results only for the player. We don't
		# care about printing random NPC's stats.
		if self.player:
			print("%s's stats are now:\n"%self.name)
			print(self.gen_stats_string())

		# Check to see if we should level up again.
		self.check_level_up()

#################################################################

	def determine_exp(self):
		'''
		Accepts no inputs.

		A dying Creature yields one-tenth of
		its level in EXP points.

		Returns this EXP value as an int.
		'''
		return self.LEVEL * 10

#################################################################

	def gen_stats_string(self):
		'''
		Accepts no inputs.

		Prints all of a Creature's stats
		to the screen. 

		Returns the stat string.
		'''

		outstr = f'LEVEL: {self.LEVEL}\n'\
			f'HP:    {self.HP}/{self.MAXHP}\n'\
			f'ATK:   {self.ATK}\n'\
			f'DEF:   {self.DEF}\n'\
			f'SPD:   {self.SPD}\n'\
			f'LCK:   {self.LCK}\n'\
			f'SNK:   {self.SNK}\n'\
			f'CHM:   {self.CHM}\n'\
			f'INT:   {self.INT}\n'\
			f'EXP:   {self.EXP}/{self.LEVEL*10}\n'\
			f'Location: {self.location}'
		
		return outstr

#################################################################

	def gen_inventory_string(self):

		outstr = '\nINVENTORY:\n'

		if len(self.inventory) == 0:
			outstr += '(empty)\n'
			return outstr

		names_and_quantities = {}

		for item in self.inventory:
			if item.name in names_and_quantities:
				names_and_quantities[item.name] += 1
			else:
				names_and_quantities[item.name] = 1

		for item_name in names_and_quantities:
			outstr += ('%s...%d\n'%(item_name,names_and_quantities[item_name]))

		return outstr

#################################################################

	def determine_response(self,other):
		'''
		Accepts a target Creature object as input.

		Returns other.CHM - self.CHM.
		'''
	
		if not isinstance(other,Creature):
			input('ERROR IN CREATURE: Trying to determine \
response, but other is not a Creature.')
			return 0
		
		return other.CHM - self.CHM
		
#################################################################
	
	def woo(self,other):
		'''
		Accepts a target Creature object as an input.

		Calculates the chance of success based on self's
		CHM and LCK stats, and determines if wooing occurs.

		Returns True if wooed, False if wooing fails.
		'''
		
		print('\n%s: I woo thee, %s!\n'%(self.name,other.name))

		response = self.determine_response(other)
		luck_factor = random.randint(0, int(self.LCK))

		if response >= 30:
			response_factor = 70
		elif abs(response) < 25:
			response_factor = 25
		else:
			response_factor = 0

		reaction = response_factor + luck_factor

		# print('we are in woo\nresponse = %d response_factor	 = %d luck_factor = %d'%(reaction,response_factor,luck_factor))

		if reaction >= 75:
			print('%s: Oh, %s, how thou wooest me! Enter my loins!\n'%(
				other.name, self.name))

			input('Mmm...\n')
			input('Oohhh...\n')
			input('Ah!\n')
			input('Yes!\n')
			input('Yes! Yes!\n')
			input('AH! AH! AH! AH! AHHH!\n')
			input('Ahh...\n')

			print('You wooed %s.\n'%other.name)	

			return True

		print('%s: Begone, knave!\n'%other.name)
		input('You failed to woo %s.\n'%other.name)

		return False
	
#################################################################

	def has(self,item):
		'''
		Accepts an Item object as an input.
		Searches Creature's inventory for that object.
		If found, returns True. If not found, returns False.
		'''
		for i in self.inventory:
			if i.__class__ == item.__class__:
				return True
		return False

#################################################################

	def equip(self,item):
		'''
		Accepts an Item object as input.

		Equips an Item from the inventory by setting
		its Active property to True.

		Returns None.
		'''

		#if isinstance(item,Weapon):

		#item.active = True

		pass

#################################################################

	def determine_weapon_value(self):
		'''
		Determines if the Creature is using a Weapon.
		If a Weapon is in the Creature's inventory, return True.
		'''

		from items.weapons.weapon import Weapon

		for item in self.inventory:
			if isinstance(item,Weapon):
				return item.get_atk_value(self)
		return 0

#################################################################
#################################################################
#################################################################

if __name__ == '__main__':

	from items.item import Item

	i = Item('weiner')
	hi_chm = Creature(CHM=80,location='Kalm')
	lo_chm = Creature(CHM=5)

	print(hi_chm.gen_stats_string())

	print(f'hi chm: {hi_chm.CHM}, lo chm: {lo_chm.CHM}\n \
	   lo chm - hi chm = {lo_chm.CHM - hi_chm.CHM}\n \
		hi resp = {hi_chm.determine_response(lo_chm)}\n \
		hi chm - lo chm = {hi_chm.CHM - lo_chm.CHM}\n \
		lo chm resp = {lo_chm.determine_response(hi_chm)}')

	print(hi_chm.determine_response(lo_chm))

	'''	
	a = Creature(ATK=5)
	b = Creature(ATK=20)
	c = Creature(ATK=75)
	d = Creature(ATK=100)


	e = Creature(HP=100000,DEF=5)
	f = Creature(HP=100000,DEF=20)
	g = Creature(HP=100000,DEF=75)
	h = Creature(HP=100000,DEF=100)

	print('def=5')

	a.attack(e)
	b.attack(e)
	c.attack(e)
	d.attack(e)

	print('def=20')

	a.attack(f)
	b.attack(f)
	c.attack(f)
	d.attack(f)

	print('def=75')

	a.attack(g)
	b.attack(g)
	c.attack(g)
	d.attack(g)

	print('def=100')

	a.attack(h)
	b.attack(h)
	c.attack(h)
	d.attack(h)


	#user = input("What is your name, traveller?\n")

	hero = Creature(
		25, #level
		99,	#exp
		15, #maxhp
		15,	#hp
		250,#attack
		5,	#defense
		15,	#speed
		80,	#luck
		1,	#sneak
		70,	#charm
		'Sammy',
		True
		)

	villain = Creature(
		35, #level
		99,	#exp
		1000, #Maxhp
		1000, #hp
		8,	#attack
		3,	#defense
		10,	#speed
		5,	#luck
		1,	#sneak
		1,	#charm
		'Bartholomew the Stanky Ferret'
		)

	pest1 = Creature()
	pest2 = Creature(SPD=50)

	hero.woo(villain)

	'''