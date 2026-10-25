words = ["ai", "python", "data"]

#  using pow(base,power)
print([pow(x,2) for x in range(2,11,2)])

""" lambda= shortcut function,map()means apply given function
on each item and then add them into dict"""
print(dict(map(lambda w: (w, len(w)), words)))

#set remove duplicate and get unique then sort AtoZ
print(sorted(set("banana")))