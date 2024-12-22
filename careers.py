'''
Nick Boni
11/20/2019

This file defines the various human classes in the game.
'''
from random import randint

from person import Person
from battleops import battle

class Peasant(Person):
	'''Peasants are the lowest, most boring, most generic class of Person.'''
	def __init__(self,name=''):
		super().__init__(name=name)
		self.generate_stats()
		self.name += ' the Peasant'

#################################################################
#################################################################
#################################################################

class Archer(Person):
	'''Archers are fast, lucky, sneaky, and intelligent. They have low DEF.'''
	def __init__(self,name=''):
		super().__init__(name=name)
		self.generate_stats()

		self.ATK = self.LEVEL + randint(5,15)
		self.DEF = self.LEVEL + randint(-15,-10)
		self.SPD = self.LEVEL + randint(5,15)
		self.LCK = self.LEVEL + randint(5,15)
		self.SNK = self.LEVEL + randint(5,15)
		self.INT = self.LEVEL + randint(5,15)

		self.check_attrs()

		self.name += ' the Archer'

#################################################################

	def chat(self,other):
		'''
		Woo an archer, and he or she will teach you
		how to hide.
		'''
		response = self.determine_response(other)

		if response <= -30:
			print(f'\n{self.name}: I\'ll shoot out thine eye! {self.name} holds up two fingers in defiance!')
			battle(other,self)
		elif abs(response) < 30:
			print("\n%s: Stay'st thou from my line of sight.\n"%self.name)
		elif response >= 30:
			print("\n%s: Thou canst climb my tree.\n"%self.name)
			action = self.test_convo(other,"Wouldst thou woo %s? (y/n) "%self.name)

			if action == 'y':
				
				if other.woo(self):
					input('%s gained 1 SNK!\n'%other.name)
					other.SNK += 1
			
			elif action == 'n':
				print('\n %s: I shall think of the curve of thine bow.\n'%self.name)

#################################################################
#################################################################
#################################################################

class Wizard(Person):
	'''Wizards are weak and slow, but lucky, charming, and intelligent.'''
	def __init__(self,name=''):
		super().__init__(name=name)
		self.generate_stats()

		self.DEF = self.LEVEL + randint(-25,-10)
		self.SPD = self.LEVEL + randint(-25,-10)
		self.LCK = self.LEVEL + randint(10,40)
		self.CHM = self.LEVEL + randint(10,40)
		self.MP = 10 + (self.LEVEL*2)
		self.name += ' the Wizard'

		self.check_attrs()

	def chat(self,other):
		'''Woo a wizard and learn a spell!'''
		response = self.determine_response(other)

		if response <= -30:
			input("\n%s: A hex upon thee!"%self.name)
			battle(other,self)
		elif abs(response) < 30:
			input("\n%s: I have much studying to do.\n"%self.name)
		elif response >= 30:
			print("\n%s: I shall teach thee a spell!\n"%self.name)			

			action = self.test_convo(other,"Wouldst thou learn an incantation from %s? (y/n) "%self.name)

			if action == 'y':
				input("\n%s: Unravel'st thou mine scroll!"%self.name)
				input('\n%s gained 1 INT!\n'%other.name)
				other.INT += 1				
			elif action == 'n':
				input('%s: Then away with thee!\n'%self.name)				


#################################################################

class Elder(Person):
	'''Elders are very high level, but very weak and slow.'''
	def __init__(self,name=''):
		super().__init__(name=name)
		self.generate_stats()

		self.LEVEL = randint(60,100)
		self.ATK = self.LEVEL + randint(-50,-20)
		self.DEF = self.LEVEL + randint(-50,-20)
		self.SPD = self.LEVEL + randint(-65,-35)
		self.name += ' the Elder'

		self.check_attrs()

	def chat(self,other):
		'''Woo an Elder, and enter a restorative sleep.'''
		response = self.determine_response(other)

		if response <= -30:
			input('\n%s: Cur of youth!\n%s spits on thee.\n'%(self.name,self.name))
		elif abs(response) < 30:
			input('\n%s looks upon thee with a rheumy eye.\n'%self.name)
		elif response >= 30:
			input("\n%s: Thou remind'st me of mine great grandson!"%self.name)
			input("%s: In mine youth I lived the rambling life that thou doth embody."%self.name)
			input('%s: When the Phoenician horde arrived on the doorstep of mine homestead . . . '%self.name)
			input('. . .')
			input('. . .')
			input('. . .')
			input("Thou fell'st to a restful sleep. HP restored to maximum.")
			hero.HP = hero.MAXHP

#################################################################

class Warrior(Person):
	'''Warriors are high level, powerful, and defensive,
	but slow and clumsy.'''
	def __init__(self,name=''):
		super().__init__(name=name)
		self.generate_stats()

		self.LEVEL = randint(30,70)
		self.ATK = self.LEVEL + randint(20,50)
		self.DEF = self.LEVEL + randint(15,40)
		self.SPD = self.LEVEL + randint(-15,5)
		self.SNK = self.LEVEL + randint(-30,-20)
		self.name += ' the Warrior'

		self.check_attrs()

	def chat(self,other):
		'''Woo a Warrior, and learn of battlefield exploits.'''
		response = self.determine_response(other)

		if response <= -30:
			input('\n%s: Foreigner and traitor!'%self.name)
			battle(other,self)
		elif abs(response) < 30:
			input('\n%s brushes past thee rapidly.'%self.name)
		elif response >= 30:
			action = self.test_convo(other,'\n%s: Friend and comrade! Wouldst thou hear of my latest campaign? (y/n) '%self.name)

			if action == 'y':
				input('\n%s: May thy sword smash thy enemies!'%self.name)
				input("\n%s gained 1 ATK!"%other.name)
				other.ATK += 1
			elif action == 'n':
				input('\n%s: Hast thou no stomach for the field of war?'%self.name)


#################################################################

class Monk(Person):
	'''Monks are strong and intelligent.'''
	def __init__(self,name=''):
		super().__init__(name=name)
		self.generate_stats()

		self.LEVEL = randint(50,90)
		self.ATK = self.LEVEL + randint(5,15)
		self.INT = self.LEVEL + randint(10,30)
		self.name += ' the Monk'

		self.check_attrs()

	def chat(self,other):
		'''Woo a Monk, and learn the secrets of the mind.'''
		response = self.determine_response(other)

		if response <= -30:
			print('\n%s: Thou indulgest in carnalities of mind and body. Begone with thee.'%self.name)
			input('\n%s lost 1 INT!'%other.name)
			other.INT -= 1			
		elif abs(response) < 30:
			input('\n%s meditates in silence and does not greet thee.'%self.name)
		elif response >= 30:
			
			action = self.test_convo(other,'\n%s, seated in full lotus, beckons thee to an adjacent mat. Wilt thou join? (y/n) '%self.name)

			if action == 'y':
				input('\n%s: He who understands his own mind understands all.'%self.name)
				input('\n%s gained 1 INT!'%other.name)
				other.INT += 1
			elif action == 'n':
				input('%s: Thou art trapped in the clutter of thine own mind.'%self.name)

#################################################################

class Priest(Person):
	def __init__(self, name=''):
		super().__init__(name=name)
		self.generate_stats()
		self.name += ' the Priest'

	def chat(self, other):
		input(f'{self.name}: Join the church and pay alms.')

#################################################################

if __name__ == '__main__':

	from fileops import load_file

	hero = load_file()
	hero.CHM = 100

	x = Person(name='doofus')
	print('\n %s'%x.name)
	print(x.gen_stats_string())

	y = Peasant(name='roofdus')
	print('\n %s'%y.name)
	print(y.gen_stats_string())

	a = Archer(name='Borkus')
	print('\n %s'%a.name)
	print(a.gen_stats_string())

	wiz = Wizard()
	print('\n %s'%wiz.name)
	print(wiz.gen_stats_string())

	e = Elder()
	print('\n %s'%e.name)
	print(e.gen_stats_string())

	war = Warrior()
	print('\n %s'%war.name)
	print(war.gen_stats_string())

	m = Monk()
	print('\n %s'%m.name)
	print(m.gen_stats_string())

	print(x.name)
	print(x.gen_stats_string())

	print(a.name)
	print(a.gen_stats_string())

	print(wiz.name)
	print(wiz.gen_stats_string())

	print(war.name)
	print(war.gen_stats_string())

	if input('Wilt thou chat with %s? '%a.name) == 'y':
		a.chat(hero)
		
	if input('Wilt thou chat with %s? '%e.name) == 'y':
		e.chat(hero)

	if input('Wilt thou chat with %s? '%wiz.name) == 'y':
		wiz.chat(hero)

	if input('Wilt thou chat with %s? '%war.name) == 'y':
		war.chat(hero)

	if input('Wilt thou chat with %s? '%m.name) == 'y':
		m.chat(hero)