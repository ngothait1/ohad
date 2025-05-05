# Final Project for beginners
import  time

print("Hello, This is my final project")
name = str((input("What is your name?")))

print("Hi " + name + ", nice to meet you")
print("This is a special calculator, I would need two numbers from you")

number1 = int(input("First number:"))
number2 = int(input("Second number:"))

print("Thank you for putting in your numbers, "+ str(number1) +" and " + str(number2))

evodd1 = ""
evodd2 = ""
error_msg = "An error had occured, please try again"
result = 0

if number1 % 2 == 0:
    evodd1 = "even"
else:
    evodd1 = "odd"

if number2 % 2 == 0:
    evodd2 = "even"
else:
    evodd2 = "odd"

print("I can see that the first number is " + evodd1 + " And the second is " + evodd2)

if evodd1 == "even" and evodd2 == "even":
    print("So both are even")
elif evodd1 == "odd" and evodd2 == "odd":
        print("So both are odd")
elif evodd1 == "odd" and evodd2 == "even":        
         print("So one of them is odd, and one is even")
elif evodd1 == "even" and evodd2 == "odd":        
         print("So one of them is odd, and one is even")

selection = str(input("Operator (+, -, *, /):"))

if selection == "+":
     result = number1 + number2
     print(str(number1) + selection + str(number2) + " = " + str(result))
elif selection == "-":
     result = number1 - number2 
     print(str(number1) + selection + str(number2) + " = " + str(result))
elif selection == "*":
     result = number1 * number2 
     print(str(number1) + selection + str(number2) + " = " + str(result))

elif selection == "/":
     Num_type = input("You chose division, should the result be integer? (y/n)")
     if Num_type =="y":
           if number2 == 0:
                 print("Error: number2 is zero")
                 print(error_msg)
           else: result = number1 / number2  
     elif Num_type == "n":  
            result = float(result)
            result = number1 / number2 
            print(str(number1) + selection + str(number2) + " = " + str(result))
elif selection != "+" or "-" or "*" or "/":
      print("Error: This Operator is not supported")
      print(error_msg)

print("Thank you ohad for using the calculator on " + str(time.ctime()))