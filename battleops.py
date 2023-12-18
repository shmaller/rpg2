'''
Battle operations:
- battle
- take_battle_items
'''
from fileops import GAME_OVER

def battle(*arg):
	'''
	Enters the battle sequence. 
	
	Accepts a list of combatants
	where the first index is the player, and indicies 
	2, 3, . . ., n are NPC enemies. 
	
	Returns None when only the 
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