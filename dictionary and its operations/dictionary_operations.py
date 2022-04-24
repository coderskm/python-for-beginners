d = {1:"monday", 2:"tuesday", 3:"wednesday", 4:"thursday", 5:"friday", 6:"saturday", 7:"sunday"}
print(d)
print(type(d))
d[8] = "holiday"
d[9] = "today"
d[10] = "yesterday"
print(d)
print(d[6])
print(d.get(3,'NA'))
print(d.get(12))
print(d.items())
print(d.keys())
print(d.values())

print(len(d))

#removing pair :- 
print(d.pop(1))
del d[7]
print(d)
print(d.popitem())

