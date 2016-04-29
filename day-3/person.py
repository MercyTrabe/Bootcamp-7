class Person(object):

	people_count = 0

	def __init__(self, name, age):
		self.name=name
		self.age=age
		Person.people_count += 1
	def say_hello(self):
		return "Hello, I'M {} AND {} Y/O".format(self.name,self.age)

	def  __repr__(self):
		return "<{} ,{}>".format(self.name,self.age)