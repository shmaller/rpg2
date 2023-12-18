'''
Nick Boni
7/2/19

This class defines the Hero.
'''
from person import Person

class Hero(Person):
	def __init__(self,name=''):
		super().__init__(name=name)
		self.player = True

#################################################################

	def generate_main_character(self):
		'''
		No inputs.

		Sets stats of the Hero object. Prompts the user
		to select a specialization. Based on the choice, 
		gives certain stats a boost. Only called when
		starting a new file.
		
		Returns None.
		'''
		self.name = input('What is thy name? ')

		# Prompt the user to select a specialty.
		print('%s, what is thy calling?'%self.name)

		try:
			specialty = int( input('\
			1: Strength and perseverance.\n\
			2: Slyness and deception.\n\
			3: Beguiling the ladyfolk.\n\
			4: Luck build???\n'
			) )

			if not specialty in range(1,5): raise ValueError

		except:
			print('Thy calling bodes not well for thy time in this world.\n')
			return self.generate_main_character()

		# Strength and perseverance!
		if specialty == 1:
			self.MAXHP += 5
			self.HP = self.MAXHP
			self.ATK += 5
			self.DEF += 5

		# Slyness and deception!
		elif specialty == 2:
			self.SPD += 5
			self.LCK += 5
			self.SNK += 5
			self.INT += 5

		# Beguiling the ladyfolk!
		elif specialty == 3:
			self.ATK += 5
			self.LCK += 5
			self.CHM += 30

		# Hell yeah luck build
		elif specialty == 4:
			self.LCK += 45
			
		print('Lo, %s: you begin thus:\n'%self.name)
		print(self.gen_stats_string())

#################################################################

if __name__ == "__main__":

	hero = Hero()
	hero.generate_main_character()