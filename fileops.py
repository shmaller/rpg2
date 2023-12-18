'''
File operations:
load_game_or_new_game
save_file
load_file
GAME_OVER
'''
def load_game_or_new_game():
	'''
	No inputs.

	Checks to see if a save file exists. If so, prompts user to
	load the game, or start a new file. If no file exists, creates
	a new file.

	Returns Hero with stats listed in save file.
	'''
	import os
	from hero import Hero

	if not os.path.exists('save_data.txt'):
		input('Press Enter to start a new file.')
		hero = Hero()
		hero.generate_main_character()
		save_file(hero)
		return hero
	else:
		print('Wouldst thou like to load a file, or start a new one?\n')
		
		load_or_new = input("Typeth 'L' to load, or 'N' to start a new file. ").upper()

		if not (load_or_new == 'L' or load_or_new == 'N'):
			input('\nThat thou mayest not do.\n')
			return load_game_or_new_game()

		if load_or_new == 'L':
			return load_file()
			
		elif load_or_new == 'N':
			print('\nA WARNING TO THOU: starting a new file will overwrite thine old one.\n')
			sure = input('Art thou sure? Y/N ').upper()

			if not (sure == 'Y' or sure == 'N'):
				input('\nThou art not certain.\n')
				return load_game_or_new_game()

			if sure == 'Y':
				hero = Hero()
				hero.generate_main_character()
				save_file(hero)
				return hero
			elif sure == 'N':
				return load_game_or_new_game()

#################################################################

def save_file(hero):
	'''
	Accepts Hero object as input.
	
	Saves Hero's name and
	stats to the save file. 
	
	Returns None.
	'''
	with open('save_data.txt','w') as f:
		f.write(hero.name +'\n')
		for line in hero.gen_stats_string():
			f.write(line)

#################################################################

def load_file():
	'''
	No inputs.

	Creates a Hero object which is 
	the Hero, reads stats from save file, and populates
	the Hero's attributes with those stats.

	Returns Hero object.
	'''
	from hero import Hero

	hero = Hero()

	with open('save_data.txt') as f:
		hero.name = f.readline().strip()

		for line in f:
			line_list = line.strip().split(':')
			trait = line_list[0].strip()
			value = line_list[1].strip()

			# HP is formatted 'current/max', and we want to
			# know the current quantity
			if trait == 'HP':
				hp_list = value.split('/')
				setattr(hero,'HP',int(hp_list[0]))
				setattr(hero,'MAXHP',int(hp_list[1]))
				continue				

			elif trait == 'EXP':
				exp_list = value.split('/')
				setattr(hero,'EXP',int(exp_list[0]))
				continue

			elif trait == 'Location':
				setattr(hero,'location',value)
				continue

			value = int(line_list[1])

			setattr(hero,trait,value)
	

	print('File loaded: %s\n'%hero.name)
	print(hero.gen_stats_string())

	return hero

#################################################################

def GAME_OVER():
	'''No inputs. Prints GAME OVER. The user must choose to load or quit. No return value.'''

	print(
		' ' + '*'*11 + ' ' + '\n' +
		'| GAME OVER |' + '\n' +
		' ' + '*'*11 + ' ' + '\n'
		)

	what_now = input("Continue? (y/n) ").upper().strip()

	if what_now == 'Y':
		return load_game_or_new_game()			
	elif what_now == 'N':
		quit()
	else:
		input('\nThat thou mayest not do.\n')
		return GAME_OVER()