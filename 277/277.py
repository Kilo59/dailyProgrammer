input = ['4 8', '1536 78360', '51478 5536', '46410 119340', '7673 4729', '4096 1024']
solution_key = ['1 2', '64 3265', '25739 2768', '7 18', '7673 4729', '4 1']
solution = []
###########################################################################
##		SOLUTION
###########################################################################


###########################################################################
##		CHECK SOLUTION
###########################################################################
if solution.length != solution_key.length:
	print('*Number of solutions does not match the expected number')
else:
	for index, (attempt, answer) in enumerate(zip(solution, solution_key)):
		print(str(index)+': ', end="")
		if attempt == answer:
			print('CORRECT! ')
			print(answer)
		else:
			print('INCORRECT!')
			print(answer)
			print('X', attempt)
