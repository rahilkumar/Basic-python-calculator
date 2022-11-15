first = float(input("Enter first numer => "))
Second = float(input("Enter the second number => "))
opr = str(input("Enter the operation 1'11'(+,-,*,/) => "))

if opr == "+":
    total = first + Second
elif opr == "-":
    total = first - Second
elif opr == "*":
    total = first * Second
elif opr == "/":
    total = first / Second
else:
    total = str("PLease try again and enter a vaild operation/number")

print (total)