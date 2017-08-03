import pdb

class ProjectEuler: 

	# Problem 1: If we list all the natural numbers below 10 that are multiples
	# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
	# Find the sum of all the multiples of 3 or 5 below 1000.
	def problem_1(self, counter):
		value = 0
		for i in range(3, counter): # add one to counter to allow user to input the inclusive end number 
			if i % 3 == 0 or i % 5 == 0:
				value += i
		return value		


x = ProjectEuler()
print x.problem_1(1000) 