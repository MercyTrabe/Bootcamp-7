'''def hello(name,age):
	
	 explains
	 
	return "I am {}, AND iAM {}".format(name,age)
people = [("jane",23),("joe,3")("becky.8")]'''


def super_sum(*args):
	
	total=0
	for i in args:
		total += i
	return total
print(super_sum(10,20))
print(super_sum(1,4,5,7))
a=[10, 40,60,10, 40,60]
print (super_sum(*a))



def hello_again(**kwargs):
	return "I am {}, am I'm {}".format(kwargs['name'],kwargs['age'])
print(hello_again(name='joe',age=30))
print(hello_again(name='jane',age=23))

joe = {'name':'joe','age':30}
print(hello_again(**joe))
print(hello_again(name="joe",age=89))	



