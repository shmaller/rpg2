'''
Printing operations.
- print_title_screen
- get_in_game_text
'''

def print_title_screen():
	'''Prints the title of the game to the screen. No return value.'''

	print('*'*30 + '\n' +
		'|' + ' '*28 + '|' + '\n' +
		'|' + ' '*6 + 'ENTER THE DRAGON' + ' '*6 + '|' + '\n' +
		'|' + ' '*28 + '|' + '\n' +
		'*'*30
		)
	
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