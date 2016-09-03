input = ['4 8', '1536 78360', '51478 5536', '46410 119340', '7673 4729', '4096 1024']
solution_key = ['1 2', '64 3265', '25739 2768', '7 18', '7673 4729', '4 1']
solution = []
###########################################################################
##		SOLUTION
###########################################################################
solution = solution_key

###########################################################################
##		CHECK SOLUTION
###########################################################################
if len(solution) != len(solution_key):
	print('*Number of solutions does not match the expected number')
else:
	for index, (attempt, answer) in enumerate(zip(solution, solution_key)):
		print(str(index+1)+': ', end="")
		if attempt == answer:
			print('CORRECT! ', end="")
			print('\t', answer)
		else:
			print('INCORRECT!', end="")
			print('\t',answer)
			print('\tX', attempt)
