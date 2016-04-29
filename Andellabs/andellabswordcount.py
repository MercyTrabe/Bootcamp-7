


# For example for the input "olly olly in come free"





def words(A):
  dictionary = {}
  
  for i in A.split():
    if i.isdigit():
      i = int (i)


    if i in dictionary:
      dictionary[i]  += 1
    else:
      dictionary[i] = 1
      
  return dictionary


