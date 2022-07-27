sub1 = int(input("Enter the marks of your subject 1: "))
sub2 = int(input("Enter the marks of your subject 2: "))
sub3 = int(input("Enter the marks of your subject 3: "))
if sub1 < 33 or sub2 < 33 or sub3 < 33:
    print("your are fail due to less marks")
elif (sub1 + sub2 + sub3/3) < 40:
    print("you are fail due to poor percentage")
else:
    print("you are pass")
