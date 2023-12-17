'''
Nicholas Boni
08/26/2022

This file defines the Arrows in the game. These items are all 
Ammo for Bow Weapons. Each Bow has a designated Arrow. If the 
appropriate Arrow is in the user's inventory, the Bow provides
its Attack Boost. If not, the Bow's Attack Boost is zero.
'''

from item import Item

#################################################################

class Stone(Item):
	def __init__(self):
		Item.__init__(self,'Stone',0,False,False,'A common pebble.')

#################################################################

class Arrow(Item):
	def __init__(self):
		Item.__init__(self, 'Arrow',1,False,False,'A slender shaft of wood with a broad, piercing iron tip. Fletched with soft, beautiful feathers the color of linen and rich loam.')

#################################################################

class Bolt(Item):
	def __init__(self):
		Item.__init__(self,'Bolt',5,False,False,'A thick wooden bolt fletched for use in a Crossbow. The arrowhead has four razor-sharp blades which cut a horrific, cross-shaped hole in the target.')

#################################################################