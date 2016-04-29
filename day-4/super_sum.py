

def super_sum(*args):
 
	'''
	Return a sum of numbers.
	e.g

	super_sum([1,2,3])==> 6
	super_sum([1,2,3])==> 6
	super_sum([10] [10,20,30])==>6
	'''
	total = 0
	if not args:
		return 0

	else:
		for x in args:
			if type(x)==list:
				total+=sum(x)
			
			elif type(x)==str:
				return 0
			else:
				total+=x
		return total


	
		
		
