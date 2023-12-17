'''
Nick Boni
10/18/2020

This file lays out the common items of the game.
'''

from item import Item

#################################################################

class Skull(Item):
	def __init__(self):
		Item.__init__(self,'Skull',0,False,False,'Alas!')

#################################################################

class Lantern(Item):
	def __init__(self):
		Item.__init__(self,'Lantern',5,False,False,'An oil latern which lights thy path.')

#################################################################
