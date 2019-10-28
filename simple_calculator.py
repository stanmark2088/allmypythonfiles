import sys

while True:
     num1 = input("num1: ")

     if not num1.isdigit():
          sys.exit("invalid number")

     op = input("Operator: ")
     num2 = input("num2: ")

     if not num2.isdigit():
          sys.exit("invalid number")

     if op == "+":
          print(int(num1) + int(num2))
     elif op == "-":
          print(int(num1) - int(num2))
     elif op == "/":
          print(int(num1) / int(num2))
     elif op == "*":
          print(int(num1) * int(num2))
     else:
          print("Invalid Operator")
     



     

