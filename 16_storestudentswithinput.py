s1 = int(input("Enter first student marks"))
s2 = int(input("Enter second student marks"))
s3 = int(input("Enter third student marks"))
s4 = int(input("Enter forth student marks"))
s5 = int(input("Enter fifth student marks"))
s6 = int(input("Enter sixth student marks"))
s7 = int(input("Enter seventh student marks"))
l1 = [s1, s2, s3, s4, s5, s6, s7] # here we can store data in list with two different ways
# l1 = [f'{f1}, {f2}, {f3}, {f4}, {f5}, {f6}, {f7}']
l1.sort()
l1.reverse()
print(l1)