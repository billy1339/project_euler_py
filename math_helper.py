import math

class Helper :

	# def __init__():

	@staticmethod
	def is_palendrome(n):
		r = str(n)[::-1]
		i = 0 
		for i in xrange(1, len(str(n))):
			if str(n)[i] != str(r)[i]:
				return False
			i+=1
		return True

	@staticmethod
	def is_prime_depreciated(n):
		c = 2
		while(c <= math.ceil(n / 2)):
			if n % c == 0:
				return False
			c += 1
		return True 
	
	@staticmethod
	def is_prime( n ):
		if n == 2:
			return True
		elif n % 2 == 0:
			return True
		
		i = 3
		range = int( math.sqrt(n) ) + 1
		while( i < range ):
			if( n % i == 0):
				return 0
			i += 1
		return 1


	@staticmethod
	def get_product(x):
		p = 1
		for i in x:
			p *= i 
		return p

	@staticmethod
	def first_divisor(n):
		for i in range(2, n + 1):
			print i 
			if n % i == 0:
				print "divisor"
				return i

	@staticmethod
	def square_of_sum(n):
		s = 0
		for i in range(1, n + 1):
			s += i
		return s * s


	@staticmethod
	def sum_of_squares(n):
		s = 0
		for i in range(1, n + 1):
			s += i * i
		return s 


