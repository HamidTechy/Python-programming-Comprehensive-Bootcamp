marks = int(input("enter your marks here"))

if marks >= 90:
    grades = "ex"
elif marks >= 80:
    grades = "A"
elif marks >= 70:
    grades = "B"
elif marks >= 60:
    grades = "C"
elif marks >= 50:
    grades = "D"
else:
    grades = "f"
print("your Grade is " + grades)

