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
class anagram_detector(object):

	def __init__(self, string_input):
		self.string_input = string_input
		self.anagram_candidate = None
		self.anagram_target = None
		self.candidate_char_list = None
		self.target_char_list = None
		self.anagram_bool = None
		#pass characters to ignore
		self.parse_input(' \'\"')

	#override string method of object
	def __str__(self):
		if self.anagram_bool == False:
			return self.anagram_candidate + ' is NOT an anagram of ' + self.anagram_target
		elif self.anagram_bool == True:
			return self.anagram_candidate + ' is an anagram of ' + self.anagram_target
		else:
			return self.anagram_candidate + ' ? ' + self.anagram_target

	#parse input on object instantiation
	def parse_input(self, ignore):
		split_values = [x.strip() for x in self.string_input.split(" ? ")]
		self.anagram_candidate = split_values[0]
		self.anagram_target = split_values[1]
		self.candidate_char_list = [x for x in split_values[0].lower() if x not in ignore]
		self.target_char_list = [x for x in split_values[1].lower() if x not in ignore]
		return

	def anagram_check(self):
		self.list_length_check()
		self.char_check()
		#if no checks have failed, assume anagram
		if self.anagram_bool != False:
			self.anagram_bool = True
		return

	#compares the lengths of two lists consisting of only lowercase characters of the anagram_target and anagram_candidate. If lengths are different, the pair is not an anagram and the test fails.
	def list_length_check(self):
		if len(self.candidate_char_list) != len(self.target_char_list):
			self.failed_test()
		return

	#sort character lists and compare them. If lists are not equal the pair is not an anagram.
	def char_check(self):
		if sorted(self.candidate_char_list) != sorted(self.target_char_list):
			self.failed_test()
		return

	def failed_test(self):
		self.anagram_bool = False
		return
#END CLASS DEFINITION

###########################################################################
##		EXECUTE SOLUTION
###########################################################################
for index, item in enumerate(input1):
	item = anagram_detector(item)
	print(index+1, item)
	item.anagram_check()
	print(index+1, item)
	print('-' * (index + 1) )