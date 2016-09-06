"""
https://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/
A fraction exists of a numerator (top part) and a denominator (bottom part) as you probably all know.
Simplifying (or reducing) fractions means to make the fraction as simple as possible.
Meaning that the denominator is a close to 1 as possible.
This can be done by dividing the numerator and denominator by their greatest common divisor.
"""
input1 = ['4 8', '1536 78360', '51478 5536', '46410 119340', '7673 4729', '4096 1024']
solution_key = ['1 2', '64 3265', '25739 2768', '7 18', '7673 4729', '4 1']
solution = []
###########################################################################
##		SOLUTION
###########################################################################
#1. Split values, convert to ints
split_values = []
for index, i in enumerate(input1):
	#split values, store in 2 item list
	split_values.append(input1[index].split())
	#convert to ints
	split_values[index][0] = int(split_values[index][0])
	split_values[index][1] = int(split_values[index][1])

#2. Find Greatest Common Factor/Divisor
def get_factors(number):
	#use list comprehension
	return [x for x in range(1, number+1) if number % x == 0]
#use get_factors to find the GCF
def greatest_common_factor(a, b):
	a_factrs = get_factors(a)
	b_factrs = get_factors(b)
	common_factors = [x for x in a_factrs if x in b_factrs]
	#print('GCF', max(common_factors))
	return max(common_factors)

#3.Simplify Fraction (divide by GFC)
def simplify_fraction(a, b):
	gcf = greatest_common_factor(a, b)
	return str(int(a/gcf))+' '+str(int(b/gcf))

#4.Iterate over values and apply solution (append to solution list)
for a_set in split_values:
	solution.append(simplify_fraction(a_set[0], a_set[1]))

###########################################################################
##		CHECK SOLUTION
###########################################################################
if len(solution) != len(solution_key):
	print('*Number of solutions does not match the expected number')
else:
	for index, (attempt, answer) in enumerate(zip(solution, solution_key)):
		print(str(index+1)+': ', end="")
		if attempt == answer:
			print('CORRECT!', end="")
			print('\t', answer)
		else:
			print('INCORRECT!', end="")
			print('\t',answer)
			print('\t\tX', attempt)
