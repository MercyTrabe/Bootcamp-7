def data_type(x):
	
	if type(x) == str:
		return  len(x)
	if x is None:
		return "no value"
		
	if type(x) == bool:
		return x
		
	if type(x) == int:
		if x < 100:
			return "less than 100"
		if x ==  100:
			return "equal to 100"
		if x >  100:
			return "more than 100"
		
	if type(x) == list:
		if len(x) >=3:
			return x[2]
		else:
			 return None

		
	



print(data_type(6))

print(data_type("Mercy"))

print(data_type(False))

print(data_type(None))

print(data_type([1,2,7]))


