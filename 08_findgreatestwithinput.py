num1 = int(input("enter a number 1: "))
num2 = int(input("enter a number 2: "))
num3 = int(input("enter a number 3: "))
num4 = int(input("enter a number 4: "))
if num1 > num2:
    f1 = num1
else:
    f1 = num2
if num3 > num4:
    f2 = num3
else:
    f2 = num3
if f1 > f2:
    print(f"{f1} is greater")
else:
    print(f"{f2} is greater")
