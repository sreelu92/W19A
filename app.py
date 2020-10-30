import addition
import division
import multiplication
import subtraction

print("Python Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("Please enter your selection:")

choice=input()

print("Enter your first number")
first_number=float(input())
print("Enter your second number")
second_number=float(input())


if(choice=='1'):
    print("Your result: ", addition.adding(first_number,second_number))
elif(choice=='2'):
    print("Your result: ", subtraction.subtracting(first_number,second_number))
elif(choice=="3"):
    print("Your result: ", multiplication.multiplying(first_number,second_number))
elif(choice=='4'):
    print("Your result: ", division.dividing(first_number,second_number))
else:
    print("Invalid input")
