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
	def is_prime(n):
		c = 2
		while(c <= math.ceil(n / 2)):
			if n % c == 0:
				return False
			c += 1
		return True 
	
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