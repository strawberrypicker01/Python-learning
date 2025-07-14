try:
    num1, num2, = eval(input("Enter 2 numbers, seperated by a comma: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Division by zero is not possible.")
except SyntaxError:
    print("Comma is missing, Please enter numbers seperated by comma like: 1,2")
except:
    print("Wrong input.")
else:
    print("No exceptions were thrown.")
finally:
    print("This is executed no matter what.")