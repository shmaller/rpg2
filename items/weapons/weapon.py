'''
Nick Boni
10/18/2020

This file lays out the base class for all Weapons in the game.
'''

from items.item import Item

# imports * from careers, * from person, * from creature,
# battle and determine_response from mechanics,
# randint, choice, choices from random
from creatures.people.careers import *

class Weapon(Item):
	'''A Weapon is a type of Item which may boost
	the wielder's ATK stat. Holder only receives a 
	boost if he or she is skilled in that particular 
	Weapon, as determined by his or her Career.'''

	def __init__(self,
	atk_value=0,
	condition=100,
	ammo=None):
		'''
		Initializes a Weapon object with the following unique characteristics:

		- ATK Boost
		- Condition
		- User Class

		A note on User Class:
		Weapons can only be wielded by a 
		Person with the proper Career, i.e.,
		an object of the correct Person child
		class. 
		'''
		Item.__init__(self)
		self.atk_value = atk_value
		self.condition = condition
		self.ammo = ammo
		self.user_class = None

#################################################################

	def check_user_class(self,user):
		'''Accepts a Person (or Person child class) object as input.

		If that object is of the proper Person child class to use
		this weapon, returns True. Else, returns False.'''

		if user.__class__ == self.user_class:
			return True
		return False

#################################################################

	def get_atk_value(self,user=None):
		'''Optional user input. For the majority of weapons this
		input is not necessary.

		Returns atk value property.

		This method works differently for Bows.'''

		return self.atk_value

#################################################################

	def inspect(self):
		'''
		No inputs.

		Generates a string for display which describes:
		- name
		- attack power
		- condition
		- value
		- text description

		Returns the outstring.
		'''

		outstr = '\nName: %s\n\
		Attack......%d\n\
		Condition...%d\n\
		Value.......%d\n\
		Description: %s'%(
			self.name,
			self.atk_boost,
			self.condition,
			self.value,
			self.description
			)
		return outstr