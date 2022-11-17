num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
print("enter 1 for addition")
print("enter 2 for Subtraction")
print("enter 3 for multiplication")
print("enter 4 for division")
print("enter 5 for modulus")
operator=input("your operation? ")

if operator == "1":
  print("num1+num2= ", num1+num2)

elif operator == "2":
  print("num1-num2= ", num1-num2)

elif operator == "3":
  print("num1*num2= ", num1*num2)

elif operator == "4":
  print("num1/num2= ", num1/num2)

elif operator == "5":
  print("num1%num2= ", num1%num2)

else:
  print("invalid operator")



