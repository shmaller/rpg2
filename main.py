from bestiary import *
from careers import *
from mechanics import *
from location import *
from daggers import *

if __name__ == '__main__':

	print_title_screen()

	hero = load_game_or_new_game()

	print('\nThou canst save the game at any time by typing "save", and quit by typing "quit".\n')

	while True:

		action = input('\nWilt thou chat with the locals, or venture into the wilderness? (c/w) ').lower()
		
		if action == 'c':
			person = input('\nWilt thou speak with the archer or the mage? (a/m) ')

			if not (person == 'a' or person == 'm'):
				continue

			if person == 'a':
				chatter = Archer(hero)

			elif person == 'm':
				chatter = Wizard(hero)

			chatter.chat(hero)

		elif action == 'w':
			locale = input('Wilt thou go to the cave, or the field? (c/f) ')
			if locale == 'c':
				hero.inventory.append(SteakKnife())
				if input('Inspect SteakKnife? (y/n) ') == 'y':
					print(hero.inventory[0].inspect())
				r = Rat()
				g = Goblin()
				battle(hero,r)
				battle(hero,g)

				further = input('Wilt thou delve further into the cave? (y/n) ')

				if further == 'y':
					g2 = Goblin()
					g3 = Goblin()
					w = Warlock()
					battle(hero,w,g2,g3)

			elif locale == 'f':
				b = Bear()
				battle(hero,b)

		elif action == 'quit':
			quit()

		elif action == 'save':
			save_file(hero)