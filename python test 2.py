def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

try:
    num1 = float(input("Please enter a number"))
    num2 = float(input("Please enter a number"))
    operator = input("Please enter any operator(+,-,*,/)")
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        result = None
        print("Invalid Input")
    if result is not None:
        print("result is:",result)

except ValueError:
    print("This is not integer,please enter integer")
except ZeroDivisionError:
    print("Cannot divide by zero")


    

