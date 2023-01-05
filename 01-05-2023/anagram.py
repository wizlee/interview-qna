'''
Question from memory as didn't copy the original question:
Write a function that determine whether 2 input arguments are anagram.
'''
def anagram(arg_1, arg_2):
  norm_arg_1 = str.lower(arg_1)
  norm_arg_2 = str.lower(arg_2)
  dict_1 = arr2Dict(norm_arg_1)
  dict_2 = arr2Dict(norm_arg_2)

  return "Anagram" if dict_1 == dict_2 else "No"

def arr2Dict(arr):
  dict_map = {}
  for c1 in arr:
    if c1 in dict_map:
      dict_map[c1] += 1
    else:
      dict_map[c1] = 1
  return dict_map

print(anagram("as dg", "da sg"))
print(anagram("alpaaa", "laap"))
print(anagram("this makes sense", "sense makes this"))
print(anagram("this makes sense", "sense  makes this"))
