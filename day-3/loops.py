


b=[(2,3),(3,4),(2,3),(2,3)]
'''
x:2,y:4
x:5,y:10
'''
print("{} {}".format("x","y"))
for s in b:
	
	print("{} {}".format(s[0],s[1]))



f=[(12,20,40),(10,40),(4,5,50)]

 
for w in f:
	if len(w) == 2:
	
	    print("{} {}".format(*w))
	elif len(w) == 3:

		print("{} {} {}".format(*w))
   


 
