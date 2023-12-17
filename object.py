from random import choice

class object:

	def test_name(input_name='',list_of_names_to_choose=["unnamed object"]):
		'''Takes an object's name, and if it's an empty string,
		returns a choice from a list of alternate names.'''

		if input_name == '':
			return choice(list_of_names_to_choose)
		else:
			return input_name