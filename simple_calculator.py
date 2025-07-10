#-----DAY 3-----
#THIS IS VERY BASIC CALCULATOR
#LEARNED ABOUT ARITHMETICS OPERATORS AND OPERATIONS
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))

addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
division=num1/num2 if num2!=0 else "cannot divide by 0"

print(f"\n----THIS IS BASIC CALCULATOR----")
print(f"addition of {num1} and {num2} is = {addition}")
print(f"addition of {num1} and {num2} is = {subtraction}")
print(f"addition of {num1} and {num2} is = {multiplication}")
print(f"addition of {num1} and {num2} is = {division}")



#THIS IS MORE ADVANCE CALCULATOR 
#WHERE WE CAN CHOOSE WHAT DO WE WANT TO PERFORM
print("----THIS IS BASIC CALCULATOR----")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    result = num1 + num2
    print(f"Addition of {num1} and {num2} is = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"Subtraction of {num1} and {num2} is = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"Multiplication of {num1} and {num2} is = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"Division of {num1} and {num2} is = {result}")
    else:
        print("Cannot divide by 0")
else:
    print("Invalid choice")