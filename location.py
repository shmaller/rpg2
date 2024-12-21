'''
Nick Boni
7/26/2018
'''

from careers import *
from random import choice

class Location:
	'''A Location is defined simply: it has a population, and you can go there.'''

#################################################################

	def test_name(input_name,list_of_names_to_choose):
		'''Takes an object's name, and if it's an empty string,
		returns a choice from a list of alternate names.'''

		if input_name == '':
			return choice(list_of_names_to_choose)
		else:
			return input_name

#################################################################

	def __init__(
		self,
		population,
		input_name = '',
		demographics = {},
		generic_class = Peasant,
		text_dict = {}
		):
		'''
		Generates a list of inhabitants that occupy this Location. An additional property,
		'inhabitants', is generated.

		demographics must be a dictionary of classes found in the Location. Keys are class 
		names, values are the percentage of Creatures in the Location of that class.

		Demographic weights must add up to 1. Child classes of Location may procedurally generate
		a population if this is not the case, but here this is mandated.

		inputs:
		self,
		hero,
		population (int),
		input name (str),
		demographics (dict),
		generic_class (class)

		No return value.
		'''

		# try:
		self.population = population
		self.demographics = demographics
		self.name = self.test_name(input_name)
		self.stuff_population_with_generic_inhabitants(generic_class)
		self.inhabitants = self.generate_inhabitants()
		self.text_dict = text_dict

		"""

		except ValueError:
			print('Error generating settlement: Each value in demographics dict must be a \n \
			positive decimal number <= 1. dict values must add \n \
			up to a number less than or equal to 1.')
			'''
			except TypeError:
				print('Error generating settlement: All values in demographics must be floats.')
			'''
		except:
			print('Unhandled error generating settlement.')

		"""

#################################################################

	def generate_inhabitants(self):
		'''
		No inputs.
		
		Given the demographic breakdown of the settlement, 
		generates a list of instances of the relevant jobs. Sets self.inhabitants
		property to this list of citizens. 
		
		Returns list of citizens.
		'''
		inhabitants = []

		for job in self.demographics:
			num_people_with_this_job = int(self.demographics[job] * self.population)
			
			for i in range(num_people_with_this_job):
				inhabitants.append(job())

		return inhabitants

#################################################################

	def stuff_population_with_generic_inhabitants(self,generic_inhabitant_class):
		'''Takes a generic inhabitant class as an input. If the 
		demographic weights in demographics don't add up to 1, 
		then this function creates an additional entry in the 
		demographics dictionary whose key is the generic inhabitant
		class, and value is the missing percentage.'''

		sum = 0

		for job in self.demographics:
			if self.demographics[job] < 0: 
				raise ValueError
			sum += self.demographics[job]

		if sum < 1:
			stuff = True
		elif sum == 1:
			stuff = False
		elif sum > 1:
			raise ValueError

		if stuff:
			self.demographics[generic_inhabitant_class] = (1 - sum)

#################################################################

	# def set_name(self,name):
	# 	'''Takes input name and assigns it to self.name property.
	# 	If self.name is an empty string, assigns a randomly-chosen
	# 	name to the settlement. Returns name as str.'''

	# 	settlement_names = ['Kalm','Jericho','Mordor','Lazi','Haaf','Loosibobo',
	# 				'Makra','Caco','Frie','Crase','Jump','Ulundi','Virginia']

	# 	if name == '':
	# 		return choice(settlement_names)
	# 	else:
	# 		return name

#################################################################

	def print_info(self):

		print(
			'Information on %s:\n\n \
			Population: %d\n \
			Demographics: \n '%(self.name,self.population)
			)

		for Creature in self.inhabitants:
			print(Creature.name)
			print(Creature.gen_stats_string())

#################################################################
'''
class Settlement(Location):

	def __init__(self):

		population = randint(10,30)
		Settlement.__init__(population)

		if sum < 1:
			self.STUFF_WITH_PERSONS = True
		elif sum == 1:
			self.STUFF_WITH_PERSONS = False
		elif sum > 1:
			raise ValueError

		if self.STUFF_WITH_PERSONS:
			self.demographics[Person] = (1 - sum)

		settlement_names = ['Kalm','Jericho','Mordor','Lazi','Haaf','Loosibobo',
					'Makra','Caco','Frie','Crase','Jump','Ulundi','Virginia']

	def generate_citizens(self,hero):
'''
#################################################################

if __name__ == '__main__':

	from fileops import load_file
	from bestiary import *
	
	hero = load_file()

	pop = randint(15,36)
	demo = {Archer: 0.4,Warrior: 0.2, Elder: 0.1}
	name = 'Kalm'

	Kalm = Location(hero,pop,name,demo)
	print('demographics = ')
	print(Kalm.demographics)
	#print(Kalm.STUFF_WITH_PERSONS)
	Kalm.print_info()

	# pes = Settlement(hero,3)
	# pes.print_info()
	# print(len(pes.demographics))

	random_citizen = choice(Kalm.inhabitants)
	print('Chose: %s'%random_citizen.name)

	random_citizen.chat(hero)

	demo2 = {Bear: 0.5,Goblin: 0.2}
	name = 'Balm'

	Balm = Location(hero,pop,name,demo2)
	print('Demographics = ')
	Balm.print_info()

	random_citizen = choice(Balm.inhabitants)
	print('Chose: %s'%random_citizen.name)

	random_citizen.chat(hero)