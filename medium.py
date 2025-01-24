# The program may not be performing calculations correctly. There are a lot of other issues with this code...can you find them??

def calculator():
    print("Welcome to the Misbehaving Calculator!")
    print("Choose operation: +, -, *, /")
    operation = input("Enter operation: ")

    try:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
    except:
        print("Invalid input! Please enter numbers only.")
        return

    try:
        if operation == "+":  
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            print("Invalid operation!")
            return
    except:
        print("Oops.")
        return
    print("Result: " + result)

calculator()
