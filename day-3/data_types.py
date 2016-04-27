def data_type(x):
	'''
	Takes in argument, x:
	-For integer, return, x **2
	-For a loat, return x/2
	-For a sting, "hello"+ X
	-For a boolean, return "boolean"
	-For a long, return the sqr root of it
	'''
	if type(x) == int:
		return x ** 2
	if type(x) == float:
		return x / 2
	if type(x) == str:
		return "Hello " + x
	if type(x) == bool:
		return "boolean"
	if type(x) == long:
		return "long" 



print(data_type(6))

print(data_type(4.4))

print(data_type("Mercy"))

print(data_type(False))

print(data_type(50 ** 40))






