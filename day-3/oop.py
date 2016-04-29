
from person import Person

p = Person('Joe',23)
p2 =Person('Joep',3)
p3 =Person('Jop',2)


a =[('Joe',23),('Joep',3),('Jop',2)]
b=[]

for name,age in a:
	person = Person(name,age)
	b.append(person)
for person in b:
	print(person.say_hello())






print(b)
print(p.say_hello())



		

	