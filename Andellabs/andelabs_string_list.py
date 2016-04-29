def string_length(x):

  list_for_string = []
  list_for_list = []
    
  if type(x) == str:
    r = len(x)
    list_for_string.append(r)
    return list_for_string


    
    for a in x:
      v =len(a)
      list_for_list.append(v)
    return list_for_list

print(string_length(['Adam', 'Frankel']))