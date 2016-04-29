

# You are presented with two arrays, all containing positive integers. One of the arrays will have one extra number, see below:

# [1,2,3] and [1,2,3,4] should return 4

# [4,66,7] and [66,77,7,4] should return 77




def find_missing(x,y):
	if len(x) and  len(y)==0:
	 	return 0
	if len(x)<len(y):
		return set(y).difference(x)
	if set(y).difference(x)==set(x).difference(y):
		return 0



	
		
print( find_missing([],[]))
print( find_missing([1,2,3],[1,2,3,4]))
print( find_missing([4,66,7],[66,77,7,4]))
print( find_missing([4,66,7],[66,7,4]))