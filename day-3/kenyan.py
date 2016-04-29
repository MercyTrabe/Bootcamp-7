 
from person import Person
class Kenyan(Person):

 	def probe(self,corrupt):

 		self.corrupt=corrupt
 	def is_corrupt(self):
 		 if self.corrupt:
 		 	return "YES"
 		 return "No"
k= Kenyan('Ann Waiguru',2)
k.probe(True)
print("Is {} corrupt? {}".format(k.name,k.is_corrupt()))
print (k.say_hello())
