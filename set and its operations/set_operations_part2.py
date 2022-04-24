s1 = {2,4,6,8}
s2 = {4,8}

#subset or not:-
print(s1.issubset(s2))
print(s2.issubset(s1))

#proper subset or not:-
print(s1>s2)

#superset or not:-
print(s1.issuperset(s2))

#disjoint or not:-
print(s1.isdisjoint(s2))