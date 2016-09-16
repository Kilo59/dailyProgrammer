#[2016-09-12] Challenge #283 [Easy] Anagram Detector
"""
r/dailyprogrammer/comments/52enht/20160912_challenge_283_easy_anagram_detector/
"""
###########################################################################
##		INPUT
###########################################################################
input1 = [      '\"wisdom\" ? \"mid sow\"',\
		'\"Seth Rogan\" ? \"Gathers No\"',\
		'\"Reddit\" ? \"Eat Dirt\"',\
		'\"Schoolmaster\" ? \"The classroom\"',\
		'\"Astronomers\" ? \"Moon starer\"',\
		'\"Vacation Times\" ? \"I\'m Not as Active\"',\
		'\"Dormitory\" ? \"Dirty Rooms\"']
###########################################################################
##		SOLUTION
###########################################################################
class anagram_pair(object):

	def __init__(self, string_input, sentence=None, anagram_target=None, anagram_bool=None):
		self.string_input = string_input
		self.sentence = None
		self.anagram_target = None
		self.anagram_bool = None
		self.parse_input()


#override string method of object
	def __str__(self):
		if self.anagram_bool == False:
			return self.sentence + ' is NOT an anagram of ' + self.anagram_target
		elif self.anagram_bool == True:
			return self.sentence + ' is an anagram of ' + self.anagram_target
		else:
			return self.sentence + ' ? ' + self.anagram_target


	def parse_input(self):
		split_values = [x.strip() for x in self.string_input.split(" ? ")]
		self.sentence = split_values[0]
		self.anagram_target = split_values[1]
		return


	def anagram_check(self):
		self.character_check()
		self.repeat_character_check()
		self.word_shuffle_check()
		#if all no checks have failed, assume anagram
		if self.anagram_bool != False:
			self.anagram_bool = True
		return


	def failed_test(self):
		self.anagram_bool = False


	def character_check(self):
		flags = 0
		ignore = ' \''
		for character in self.sentence.lower():
			if character not in self.anagram_target.lower():
				flags += 1
		for character in self.anagram_target.lower():
			if character not in ignore:
				if character not in self.sentence.lower():
					print('Flag: ', character)
					flags += 1
		if flags > 0:
			self.failed_test()
		return flags


	def repeat_character_check(self):
		pass
		return


	def word_shuffle_check(self):
		pass
		return
#END CLASS DEFINITION

###########################################################################
##		EXECUTE SOLUTION
###########################################################################
for index, item in enumerate(input1):
	item = anagram_pair(item)
	print(index+1, item)
	item.anagram_check()
	print(index+1, item)
	print('-' * (index + 1) )