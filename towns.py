'''
Nick Boni
7/26/2018
'''

from location import *
from careers import *
from random import choice

"""
class Location:
	'''A Location is defined simply: it has a population, and you can go there.'''

	def __init__(
		self,
		hero,
		population,
		name = '',
		demographics={}
		):
		'''
		Generates a list of inhabitants that occupy this Location. An additional property,
		'citizenry', is generated.

		demographics must be a dictionary of classes found in the Location. Keys are class 
		names, values are the percentage of creatures in the Location of that class.

		Demographic weights must add up to 1. Child classes of Location may procedurally generate
		a population if this is not the case, but here this is mandated.
		'''

		try:
			self.hero = hero
			self.population = population
			self.demographics = demographics
			self.name = self.set_name(name)

			sum = 0

			for type_of_creature in demographics:
				if demographics[type_of_creature] < 0: 
					raise ValueError
				sum += demographics[type_of_creature]

			if sum < 1:
				self.STUFF_WITH_PERSONS = True
			elif sum == 1:
				self.STUFF_WITH_PERSONS = False
			elif sum > 1:
				raise ValueError

			if self.STUFF_WITH_PERSONS:
				self.demographics[Person] = (1 - sum)

			self.citizenry = self.generate_citizens()

		except ValueError:
			print('Error generating settlement: Each value in demographics dict must be a \n \
			positive decimal number <= 1. dict values must add \n \
			up to a number less than or equal to 1.')

		except TypeError:
			print('Error generating settlement: All values in demographics must be floats.')

		except:
			print('Unhandled error generating settlement.')

#################################################################

	def generate_citizens(self):
		'''No inputs. Given the demographic breakdown of the settlement, 
		generates a list of instances of the relevant jobs. Sets self.citizenry
		property to this list of citizens. Returns list of citizens.'''

		citizenry = []

		for job in self.demographics:
			num_people_with_this_job = int(self.demographics[job] * self.population)
			for i in range(num_people_with_this_job):
				citizenry.append(job(self.hero))

		return citizenry

#################################################################

	def set_name(self,name):
		'''Takes input name and assigns it to self.name property.
		If self.name is an empty string, assigns a randomly-chosen
		name to the settlement. Returns name as str.'''

		settlement_names = ['Kalm','Jericho','Mordor','Lazi','Haaf','Loosibobo',
					'Makra','Caco','Frie','Crase','Jump','Ulundi','Virginia']

		if name == '':
			return choice(settlement_names)
		else:
			return name

#################################################################

	def print_info(self):

		print(
			'Information on %s:\n\n \
			Population: %d\n \
			Demographics: \n '%(self.name,self.population)
			)

		for person in self.citizenry:
			print(person.name)
			print(person.gen_stats_string())

"""

#################################################################

class Settlement(Location):

	def __init__(self,hero,population,name,demographics,gen_class=Peasant):

		population = randint(10,30)
		Location.__init__(self,hero,population,name,demographics,gen_class)

		print('name = %s'%self.name)

		'''

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
	
	hero = load_file()

	pop = randint(15,36)
	demo = {Archer: 0.4, Warrior: 0.2, Elder: 0.1}
	name = 'Kalm'

	Kalm = Settlement(hero,pop,name,demo)
	print('demographics = ')
	print(Kalm.demographics)
	# print(Kalm.STUFF_WITH_PERSONS)
	Kalm.print_info()

	# pes = Settlement(hero,3)
	# pes.print_info()
	# print(len(pes.demographics))

	random_citizen = choice(Kalm.inhabitants)
	print('Chose: %s'%random_citizen.name)

	random_citizen.chat(hero)