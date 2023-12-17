'''
Nick Boni
7/19/2018

Mechanics of the game including GAME_OVER, and 
battle process.
'''

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

#################################################################

def print_title_screen():
	'''Prints the title of the game to the screen. No return value.'''

	print('*'*30 + '\n' +
		'|' + ' '*28 + '|' + '\n' +
		'|' + ' '*6 + 'ENTER THE DRAGON' + ' '*6 + '|' + '\n' +
		'|' + ' '*28 + '|' + '\n' +
		'*'*30
		)

#################################################################

def load_game_or_new_game():
	'''
	No inputs.

	Checks to see if a save file exists. If so, prompts user to
	load the game, or start a new file. If no file exists, creates
	a new file.

	Returns Creature with stats listed in save file.
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
	Accepts Hero object as input. Saves Hero's name and
	stats to the save file. Returns None.
	'''

	with open('save_data.txt','w') as f:
		f.write(hero.name +'\n')
		for line in hero.gen_stats_string():
			f.write(line)

	#return hero

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
	# hero.player = True

	with open('save_data.txt') as f:
		hero.name = f.readline().strip()

		for line in f:
			x = line.strip().split(':')
			trait = x[0].strip()

			# HP is formatted 'current/max', and we want to
			# know the current quantity
			if trait == 'HP':
				y = x[1].split('/')
				setattr(hero,'HP',int(y[0]))
				setattr(hero,'MAXHP',int(y[1]))
				continue				

			elif trait == 'EXP':
				y = x[1].strip().split('/')
				setattr(hero,'EXP',int(y[0]))
				break

			value = int(x[1])

			setattr(hero,trait,value)

	print('File loaded: %s\n'%hero.name)
	print(hero.gen_stats_string())

	return hero

#################################################################

# def generate_main_character():
# 	'''
# 	No inputs.

# 	Instantiates a Hero object. Prompts the user
# 	to select a specialization. Based on the choice, 
# 	gives certain stats a boost. 
	
# 	Returns Creature object.
# 	'''

# 	from hero import Hero

# 	name = input('What is thy name? ')

# 	# Prompt the user to select a specialty.
# 	print('%s, what is thy calling?'%name)

# 	try:
# 		specialty = int( input('\
# 		1: Strength and perseverance.\n\
# 		2: Slyness and deception.\n\
# 		3: Beguiling the ladyfolk.\n\
# 		4: Luck build???\n'
# 		) )

# 		if not specialty in range(1,5): raise ValueError

# 	except:
# 		print('Thy calling bodes not well for thy time in this world.\n')
# 		generate_main_character()
# 		return

# 	hero = Hero(name) # these three lines are weird
# 	# hero.name = name								  # here
# 	hero.player = True  							  # here

# 	# Strength and perseverance!
# 	if specialty == 1:
# 		hero.MAXHP += 5
# 		hero.HP = hero.MAXHP
# 		hero.ATK += 5
# 		hero.DEF += 5

# 	# Slyness and deception!
# 	elif specialty == 2:
# 		hero.SPD += 5
# 		hero.LCK += 5
# 		hero.SNK += 5
# 		hero.INT += 5

# 	# Beguiling the ladyfolk!
# 	elif specialty == 3:
# 		hero.ATK += 5
# 		hero.LCK += 5
# 		hero.CHM += 30

# 	# Hell yeah luck build
# 	elif specialty == 4:
# 		hero.LCK += 45
		
# 	print('Lo, %s: thou beginnest thus:\n'%hero.name)
# 	print(hero.gen_stats_string())

# 	return hero

#################################################################

def battle(*arg):
	'''Enters the battle sequence. Accepts a list of combatants
	where the first index is the player, and indicies 
	2, 3, . . ., n are NPC enemies. Returns None when only the 
	player is left standing, or when the player dies.'''

	input('\nA fight!\n')

	# Initialize a list of combatants in the fight.
	belligerents = []
	i = 0

	# Populate the list of combatants based on the 
	# indefinite list of arguments provided to the fn.
	# Prints out their HP to the screen.
	for combatant in arg:
		print("%d: %s has %d/%d HP.\n"%(i,combatant.name,combatant.HP,combatant.MAXHP))
		belligerents.append(combatant)
		if combatant.player:
			player = combatant
		i += 1

	# Player must be the first argument provided to
	# this function.
	#player = belligerents[0]

	# We now create a list with the appropriate 
	# attack order, sorted by Creature's speed.
	combatants_sorted_by_spd = sorted(belligerents, key=lambda Creature: Creature.SPD, reverse=True)

	# This is a list of Items dropped by
	# dead combatants. Only retrievable if
	# the Hero does not flee!
	spoils = []

	# This variable controls the battle loop.
	fight_on = True

	# This variable will prevent combat from continuing
	# if the user makes an input error.
	combat_error = False

	while fight_on:

		# Iterate through the combatants. Each combatant
		# gets a turn in the fight.
		for combatant in combatants_sorted_by_spd:

			# If the user makes an input error, skip
			# to the user's next turn so as not to 
			# penalize him a turn for a typo.
			if combat_error:
				if not combatant.player:
					continue
				combat_error = False

			# Logic handling user commands in a battle.
			if combatant.player:
				action = input("\nWhat wilt thou do? Type 'A' for attack or 'R' to run. ").upper()
				if not (action == 'A' or action == 'R'):
					input('\nThat thou mayest not do!\n')
					combat_error = True
					break

				if action == 'A':
					try:
						j = int( input("\nWhich foe shalt thou smite? Type 1 for the first enemy, 2 for the second, . . . ") )
						if not j > 0:
							raise ValueError

						target = belligerents[j]
				
					except (ValueError,IndexError):
						print('That foe existeth not!\n')
						combat_error = True
						break

				elif action == 'R':
					'''Checks the user's SPD stat against all opponents.
					The user can escape any Creature of a same or lower SPD,
					which stops the battle immediately. If there is a faster
					Creature than the user, the belligerents list is reduced
					to those Creatures faster than the user.'''
					player_faster_than = []
					player_slower_than = []

					for c in belligerents:
						if player.SPD >= c.SPD:
							player_faster_than.append(c)
						else:
							player_slower_than.append(c)

					# If we're faster than everyone else in the fight,
					# we get away and the battle ends.
					if len(player_slower_than) == 0:
						print('\nThou hath escaped!\n')
						return player.check_level_up()

					else:
						belligerents = [player]
						for c in player_slower_than:
						 	belligerents.append(c)

						combatants_sorted_by_spd = sorted(belligerents, key=lambda Creature: Creature.SPD, reverse=True)

						print('\nThou couldst not escape these Creatures:')

						index = 1
						for c in belligerents:
							if c.player:
								continue
							print("%d: %s has %d/%d HP.\n"%(index,c.name,c.HP,c.MAXHP))
							index += 1

						# end the turn
						break

			# Logic handling NPCs in battle.
			# All NPCs in battle are against the user.
			else:
				target = player

			combatant.attack(target)

			if target.die():
				'''If a combatant dies, we remove him from the 
				belligerents list. If it's the player, we 
				stop the battle right here. Otherwise, we 
				reprint the new list of	remaining combatants.'''

				belligerents.remove(target)
				combatants_sorted_by_spd.remove(target)
				
				# Assign appropriate EXP to the combatant
				# who killed his target.
				exp_points_gained = target.determine_exp()
				combatant.EXP += exp_points_gained
				print('%s gained %d EXP.\n'%(combatant.name,exp_points_gained))

				if target.player:
					return GAME_OVER()

				# Add the dead combatant's items
				# to the list of spoils to be collected
				# by the victor at the end of battle.
				for item in target.inventory:
					spoils.append(item)

				# If only one man is left standing,
				# the battle is over.
				if len(belligerents) == 1:
					fight_on = False
					break		

				index = 0
				for c in belligerents:
					print("%d: %s has %d/%d HP.\n"%(index,c.name,c.HP,c.MAXHP))
					index += 1

	for combatant in belligerents:
		print('%s is victorious!'%combatant.name)
		combatant.check_level_up()

	return take_battle_items(player,spoils)	

#################################################################

def take_battle_items(hero,spoils):
	'''
	Accepts a list of items dropped by combatants.

	If the list is empty, return immediately.

	Else, allow the user to choose which items to add to
	the Hero's inventory.

	Returns None.
	'''

	if len(spoils) == 0: return

	print('\nThou findest the following items among the corpses:\n')
	print('0: Take all')
	'''
	spoils_dict = {}
	i = 1
	for item in spoils:
		print("%d: %s"%(i,item.name))
		spoils_dict[i] = item
		i += 1
	'''
	# sort spoils by value, most valuable first
	spoils = sorted(spoils, key=lambda Item: Item.value, reverse=True)

	i = 1
	for item in spoils:
		print('%d: %s'%(i,item.name))
		i+=1

	items_to_take = input('\nWhich items wilt thou take? Type the numbers of those to take, separated by commas (e.g., "1,3,4"): ').strip()

	if items_to_take == '0':
		for item in spoils:
			hero.inventory.append(item)
		print('\nThy inventory is now thus:')
		input(hero.gen_inventory_string())
		return

	else:
		try:
			str_numbers = items_to_take.split(",")
			
			for str_index in str_numbers:
				hero.inventory.append( spoils[ int(str_index)-1 ] )

			print('\nThy inventory is now thus:')
			input(hero.gen_inventory_string())
			return

		except (IndexError,ValueError):
			input('\nThat is not a valid selection.')
			return take_battle_items(hero,spoils)

#################################################################

# def determine_response(conversant1,conversant2):
# 	'''
# 	Accepts a target Creature object as input.

# 	Calculates difference between self and other's
# 	CHM stats.

# 	If self's stat is much higher, other
# 	is totally bowled over.

# 	If stats are similar, other's response is neutral.

# 	If self's stat is much lower, other is repulsed.

# 	Returns 'good' if case 1, 'neutral' if case 2,
# 	or 'bad' if case 3.
# 	'''

# 	response = conversant1.CHM - conversant2.CHM

# 	# print('\n\n\nwe are in determine_response\n\n\n')
# 	# print('1 chm %d - 2 charm %d = %d response'%(conversant1.CHM,conversant2.CHM,response))

# 	if response <= -25:
# 		return 'good'	
# 	elif abs(response) < 25:
# 		return 'neutral'
# 	elif response >= 25:
# 		return 'bad'
	
#################################################################

def get_in_game_text(infile, header):
	'''
	Accepts text file containing in-game text and the relevant header as an input.

	Returns string containing relevant in-game text.
	'''

	try:
		with open(infile) as f:
			outstr = ''
			for line in f:
				if line.strip() == header:
					while True:
						relevant_text = f.readline().strip()
						if '# ' in relevant_text: # next header
							break
						elif not relevant_text: # eof 
							break
						else:
							outstr += relevant_text
					return outstr

		input(f"ERROR LOADING IN-GAME TEXT: File '{infile}' found, but header '{header}' not found.")
		return ''

	except FileNotFoundError:
		input(f"ERROR LOADING IN-GAME TEXT: In-game text file not found: '{infile}'")
		return ''

#################################################################

if __name__ == '__main__':

	oustr = get_in_game_text('ingfame.txt','## KALM')
	print(f'outstr: \'{oustr}\'')
	oustr = get_in_game_text('ingame.txt','## KALM')
	print(f'outstr: \'{oustr}\'')
	oustr = get_in_game_text('ingame.txt','## ruby')
	print(f'outstr: \'{oustr}\'')
	oustr = get_in_game_text('location_hierarchy_ideas.txt','## KALM')
	'''

	from creature import *
	from hero import Hero
	
	hero = Hero()
	print(hero)
	print(hero.gen_stats_string())
	hero.generate_main_character()

	villain = Creature(
		35, #level
		99,	#exp
		50, #Maxhp
		50, #hp
		8,	#attack
		3,	#defense
		10,	#speed
		5,	#luck
		1,	#sneak
		100, #charm
		10, #int
		'Bartholomew the Stanky Ferret'
		)

	pest1 = Creature()
	pest2 = Creature(SPD=50)

	battle(hero,pest1)

	if hero.HP == 0:
		print('\nGAME OVER')
		quit()

	if input('What wilt thou do? Walk?') == 'q':
		quit()

	battle(hero,pest1,pest2,villain)

	if input('Wilt thou woo the stanky ferret? ') == 'y':
	
		chat = hero.woo(villain)

		if chat == 'good':
			res = 'I would love to speak with you!'
		elif chat == 'neutral':
			res = 'I will speak with you.'
		else:
			res = 'Get out of my face!'

		print('%s: '%villain.name + res)

	'''