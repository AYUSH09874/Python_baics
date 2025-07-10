#step 1: take the input from the user
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))

#step 2: user comparison operators to check
print("\n----COMPARISON RESULTS----")

if num1 == num2:
    print(f"{num1} is equal to {num2}")

elif num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

#check is numbers are zero

if num1 == 0 or num2 == 0:
    print("\nat least one number is zero")
else:
    print("\nboth tha numbers are zero")
