'''
Nick Boni
7/23/2018

This file defines the Person class, upon which all
human characters in the game are based.
'''

from creature import *
from mechanics import battle

#################################################################
#################################################################
#################################################################

class Person(Creature):

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
		faction=None,
		allegiance=0
		):

		super().__init__(
				   LEVEL,
				   EXP,
				   MAXHP,
				   HP,
				   ATK,
				   DEF,
				   SPD,
				   LCK,
				   SNK,
				   CHM,
				   INT,
				   name,
				   player,
				   inventory
				   )
		
		self.faction = faction
		self.allegiance = allegiance

#################################################################

	def generate_stats(self):
		'''
		Sets stats at a random number 
		somewhere around current level.
		'''

		names = ['Mattias','Franny','Leopold','Catche','Slan','Reog',
'Frack','Lance','Samantha','Lili','Martha','Zuzu','Borb','Horatio',
'Rosecratz','Guildenstern','Chunk','Blork','Effel','Yorick', 'Puck',
'Osgood','Rank','Lelel','Bilbo','Kattiwampus']

		self.LEVEL = randint(1,100)

		if self.LEVEL <= 0:
			self.LEVEL = 1

		self.EXP = randint( 0, self.determine_exp()-1 )
		self.MAXHP = 10 + ( (self.LEVEL-5) * randint(0,3) )
		self.HP = self.MAXHP
		self.ATK = self.LEVEL + randint(-10,10)
		self.DEF = self.LEVEL + randint(-10,10)
		self.SPD = self.LEVEL + randint(-10,10)
		self.LCK = self.LEVEL + randint(-10,10)
		self.SNK = self.LEVEL + randint(-10,10)
		self.CHM = self.LEVEL + randint(-10,10)
		self.INT = self.LEVEL + randint(-10,10)
		if self.name == '':
			self.name = choice(names)

		# Intelligence is charming!
		self.CHM += (self.INT / 2)

		self.check_attrs()

#################################################################

	def get_factional_opinion(self, other):
		'''
		Accepts Person object as input.

		Checks Other's factional association,
		compares it to self's factional assocation * allegiance.

		Returns float between -100 and 100.
		'''

		if not isinstance(other,Person):
			input('ERROR IN PERSON: Trying to get factional \
opinion, but other is not a Person.')
			return 0

		if self.faction and other.faction:
			return (self.faction.opinion(other) * self.allegiance * 100)
			
		return 0
	
#################################################################

	def determine_response(self, other):
		'''
		Accepts Person object as input.

		Calculates CHM difference, and then 
		factional opinion.

		Alters Creature determine_response behavior:
		Persons also consider factional alliance in
		their response to each other.
		
		Returns sum as int.
		'''
		chm_diff = super().determine_response(other)
		factional = self.get_factional_opinion(other)

		return chm_diff + factional

#################################################################

	def chat(self,other):
		'''Chatting with generic Persons is boring.'''

		responses = ['I am extremely ugly.',
		'Dost thou smell that?',
		'I have chopped down one thousand trees in my life.',
		'Wilt thou scratch mine buttocks?',
		'Thou art a stump.',
		'Inspectum mine rectum.',
		"I shall cavort for thee! Wait, no, don't run away!"]

		response = '\n%s: '%self.name + choice(responses) + '\n'

		print(response)

#################################################################

	def test_convo(self,other,instr):
		'''User input validation for conversations with the person.'''
		action = input(instr).lower()

		if not (action == 'y' or action == 'n'):
			print('\nThou hast not answered the question!')
			self.chat(other)

		return action

#################################################################

if __name__ == '__main__':

	from faction import *

	Romans = Faction('Romans')
	Huns = Faction('Huns')

	Romans.opinions = {Huns: -0.8}
	Huns.opinions = {Romans: -0.2}

	roman = Person(name='dookie',faction=Romans,allegiance=0.3,CHM=100)
	hun = Person(name='smirkle',faction=Huns,allegiance=0.9,CHM=50)

	print(f"Roman's opinion of Hun: {roman.determine_response(hun)}\n\
Hun's opinion of roman: {hun.determine_response(roman)}")

	'''
	from mechanics import load_file
	from item import Item

	hero = load_file()

	x = Person('doofus')
	print('\n %s'%x.name)
	print(x.gen_stats_string())

	hero = load_file()

	h = Item('hotdog')
	r = Item('rock')

	choice = input('Which item wilt thou take? Type 1 for hotdog, 2 for rock')
	if choice == '1':
		hero.inventory.append(h)
	elif choice == '2':
		hero.inventory.append(r)
	else:
		print('You fool!')

	print(hero.inventory)

	for item in hero.inventory:
		print(item.name)	

	# y = Peasant(hero,'roofdus')
	# print('\n %s'%y.name)
	# print(y.gen_stats_string())

	# a = Archer(hero,'Borkus')
	# print('\n %s'%a.name)
	# print(a.gen_stats_string())

	# wiz = Wizard(hero)
	# print('\n %s'%wiz.name)
	# print(wiz.gen_stats_string())

	# e = Elder(hero)
	# print('\n %s'%e.name)
	# print(e.gen_stats_string())

	# war = Warrior(hero)
	# print('\n %s'%war.name)
	# print(war.gen_stats_string())



	print(x.name)
	print(x.gen_stats_string())

	# print(a.name)
	# print(a.gen_stats_string())

	# print(wiz.name)
	# print(wiz.gen_stats_string())

	# print(war.name)
	# print(war.gen_stats_string())

	# if input('Wilt thou chat with %s? '%a.name) == 'y':
	# 	a.chat(hero)

	# if input('Wilt thou chat with %s? '%e.name) == 'y':
	# 	e.chat(hero)

	'''