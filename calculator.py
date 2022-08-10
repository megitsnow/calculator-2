"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod,)
while True:
    input_string = input(">  ")
    if input_string == 'q':
        print("Exit")
        break
    elif len(input_string) < 3:
         print ("Not enough input")
    
    else:
        calc_input = input_string.split(' ')
        
        if len(calc_input)==3:
            operator = calc_input[0]
            num1 = calc_input[1]
            num2 = calc_input[2]
            num1 = float(num1)
            num2 = float(num2)
        if len(calc_input)==2:
            operator = calc_input[0]
            num1 = calc_input[1]
            num1 = float(num1)

        if operator == "+":
            print(add(num1,num2))

        elif operator == "-":
            print(subtract(num1, num2))

        elif operator == "*":  
            print(multiply(num1, num2))
        
        elif operator == "/":
            print(divide(num1, num2))

        elif operator == "**":
            print(square(num1))

        elif operator =="cube":
             print(cube(num1))

            
    # elif input_string == "q":
    #     break

# Replace this with your code
