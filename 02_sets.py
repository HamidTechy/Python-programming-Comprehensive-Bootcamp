# a = {3, 4, 6, 3}  # set is a collection of not repetitive elements
# print(type(a))  # set will not show repeat value of set mean not allow repeat
# print(a)
#empty set
# a = {}  # this syntax will create dictionary not empty set
# print(type(a))
a = set()  # we use this syntax to create empty set
print(type(a))
# a.add("Hamid")  # .add is used in set to add new value
# a.remove("Hamid")  # .remove is used to remove the value of set
a.add((2, 3, 4, 5))  # we can add tuples in sets but not list or dictionary in sets
print(a)

