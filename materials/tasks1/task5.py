print("Welcome to the simple calculator!")

def function():
    while True: 
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        operation = input('Select an operation: \n1 for addition \n2 for subtraction \n3 for multiplication \n4 for division\nType "exit" to quit: ')

        if operation == 'exit': 
            print("Thank you for using the calculator!")
            break
        
        def function_2(num1, operation, num2):
            if operation == '1':
                x = num1 + num2
                print(f"{num1} + {num2} = {x}")
            elif operation == '2':
                y = num1 - num2
                print(f"{num1} - {num2} = {y}")
            elif operation == '3':
                z = num1 * num2
                print(f"{num1} * {num2} = {z}")
            elif operation == '4':
                try:
                    b = num1 / num2
                    print(f"{num1} / {num2} = {b}")
                except ZeroDivisionError:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Invalid operation. Please try again.")
        
        function_2(num1, operation, num2)

function()