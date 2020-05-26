def filter_list(l):
  'return a new list with the strings filtered out'
  output = []

  for element in l:
      if type(element) != str:
          output.append(element)

  return output

print(filter_list([1,2,"a","b"]))