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
solution = []

###########################################################################
##		SOLUTION
###########################################################################
class anagram_pair(object):

#one argument
#split line function
	def __init__(self, sentence, anagram_target, anagram_bool=None):
		self.sentence = sentence
		self.anagram_target = anagram_target
		self.anagram_bool = anagram_bool

#override string method of object
	def __str__(self):
		if self.anagram_bool == False:
			return self.sentence + ' is NOT an anagrame of ' + self.anagram_target
		elif self.anagram_bool == True:
			return self.sentence + ' is an anagrame of ' + self.anagram_target
		else:
			return self.sentence + ' ? ' + self.anagram_target

	def anagram_check(self):
		flags = 0
		ignore = ' \''

		for character in self.sentence:
			if character not in self.anagram_target:
				flags += 1

		for character in self.anagram_target:
			if character not in ignore:
				if character not in self.sentence:
					print('Flag: ', character)
					flags += 1

		if flags > 0:
			self.anagram_bool = False
		else:
			self.anagram_bool = True
		return

input2 = []
input2.append( anagram_pair('\"wisdom\"', '\"mid sow\"') )
input2.append( anagram_pair('\"seth rogan\"', '\"gathers no\"') )
input2.append( anagram_pair('\"reddit\"', '\"eat dirt\"') )
input2.append( anagram_pair('\"schoolmaster\"', '\"the classroom\"') )
input2.append( anagram_pair('\"astronomers\"', '\"moon starer\"') )
input2.append( anagram_pair('\"vacation times\"', '\"i\'m not as active\"') )
input2.append( anagram_pair('\"dormitory\"', '\"dirty rooms\"') )

for index, item in enumerate(input2):
	print(index + 1, item)
	item.anagram_check()
	print(index + 1, item)
	#print(index + 1, item.anagram_bool)

input2[0].anagram_check()
print(input2[0].anagram_bool)
###########################################################################
##		CHECK SOLUTION
###########################################################################
for index, anagram_pair in enumerate(input1):
	print(index + 1, anagram_pair)
