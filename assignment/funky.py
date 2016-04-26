
def funky(a,b):
    print a+b
funky(1,4)
funky(1.2,2.3)


c=[1,2,3]
d=[5,6,7]
def funky(c,d):
    print c+d
funky(c,d)


e={1:"wendy",2:"Jane"}
f={3:"paul",4:"peter"}
def funky(e,f):
    z= dict(e.items() + f.items())
    print z
funky(e,f)